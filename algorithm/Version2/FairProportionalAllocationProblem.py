import doctest

import cvxpy


from algorithm.Version2.Allocation import Allocation
from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.FairAllocationProblem import FairAllocationProblem


class FairProportionalAllocationProblem(FairAllocationProblem):

    def __init__(self, valuation):
        super().__init__(valuation)


    def find_allocation_with_min_shering(self):
        """

        :return:
        # the test are according to the result of ver 1 in GraphCheck
        >>> v = [[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6]]
        >>> fpap =FairProportionalAllocationProblem(v)
        >>> print(fpap.find_allocation_with_min_shering())
        [[0.    0.    0.    1.   ]
         [0.    0.999 0.    0.   ]
         [1.    0.    0.999 0.   ]]
        >>> v = [[5, 2, 1.5,1], [9, 1, 3,2.5], [10, 3, 2,4]]
        >>> fpap =FairProportionalAllocationProblem(v)
        >>> print(fpap.find_allocation_with_min_shering())
        [[0.    1.    0.486 0.   ]
         [0.    0.    0.513 1.   ]
         [1.    0.    0.    0.   ]]
        """
        for consumption_graph in self.graph_generator.generate_all_consumption_graph():
            self.find_allocation_for_graph(consumption_graph)
        return self.min_sharing_allocation


    def find_allocation_for_graph(self,consumption_graph : ConsumptionGraph):
        """
        consumption_graph = consumption_graph
        matv = valuation
        len(consumption_graph) = self.num_of_agents
        len(consumption_graph[0]) = self.num_of_items
        :param consumption_graph:
        :return:
        # the test are according to the result of ver 1 in GraphCheck
        >>> v = [[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6]]
        >>> fpap =FairProportionalAllocationProblem(v)
        >>> g1 = [[0.0, 0.0, 0.0, 1], [1, 1, 1, 1], [0.0, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        None
        >>> g1 = [[0.0, 0.0, 0.0, 1], [1, 1, 1, 1], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.743]
         [0.055 1.    1.    0.031]
         [0.944 0.    0.    0.225]]
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 1, 1, 1], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.801]
         [0.    1.    1.    0.083]
         [0.999 0.    0.    0.115]]
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 1, 1, 1], [1, 1, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.908]
         [0.    0.518 1.    0.032]
         [0.999 0.481 0.    0.058]]
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 0.0, 1, 1], [1, 1, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.687]
         [0.    0.    1.    0.103]
         [1.    1.    0.    0.208]]
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 0.0, 1, 1], [1, 1, 1, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.665]
         [0.    0.    0.866 0.205]
         [0.999 1.    0.133 0.129]]
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 1, 1, 1], [1, 0.0, 0.0, 0.0]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        None
        >>> g1 = [[0.0, 0.0, 0.0, 1], [0.0, 1, 1, 1], [1, 1, 0.0, 0.0]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fpap.find_allocation_for_graph(g))
        [[0.    0.    0.    0.939]
         [0.    0.462 1.    0.06 ]
         [0.999 0.537 0.    0.   ]]
        """
        mat = cvxpy.Variable((self.num_of_agents, self.num_of_items))
        constraints = []
        # every var >=0 and if there is no edge the var is zero
        # and proportional condition
        for i in range(self.num_of_agents):
            count = 0
            for j in range(self.num_of_items):
                if (consumption_graph.get_graph()[i][j] == 0):
                    constraints.append(mat[i][j] == 0)
                else:
                    constraints.append(mat[i][j] >= 0)
                count += mat[i][j] * self.valuation[i][j]
            constraints.append(count >= sum(self.valuation[i]) / len(self.valuation[i]))
        # the sum of each column is 1 (the property on each object is 100%)
        for i in range(self.num_of_items):
            constraints.append(sum(mat[:, i]) == 1)
        """
        # the proportional condition
        count = 0
        for i in range(len(consumption_graph)):
            count = 0
            for j in range(len(consumption_graph[i])):
                count += mat[i][j] * matv[i][j]
            constraints.append(count >= sum(matv[i]) / len(matv[i]))
        """
        objective = cvxpy.Maximize(1)
        prob = cvxpy.Problem(objective, constraints)
        prob.solve()  # Returns the optimal value.
        if not (prob.status == 'infeasible'):
            alloc = Allocation(mat.value)
            alloc.round()
            if(alloc.num_of_shering() < self.min_sharing_number):
                self.min_sharing_number = alloc.num_of_shering()
                self.min_sharing_allocation = alloc.get_allocation()
        # only for doctet:
        return (mat.value)

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
