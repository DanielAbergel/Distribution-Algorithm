import doctest

import cvxpy


from algorithm.Version2.Allocation import Allocation
from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.FairAllocationProblem import FairAllocationProblem


class FairProportionalAllocationProblem(FairAllocationProblem):
    """
    this class solve Fair Proportional Allocation Problem
    she is inherited from FairAllocationProblem
    proportional definition:
    V = agents valuation
    C = all agents properties
    X = proportional allocation
    n = the number of the agents
    For all i: Vi(Xi) ≥ Vi(C) / n
    """

    def __init__(self, valuation):
        super().__init__(valuation)


    def find_allocation_with_min_shering(self):
        """
        this function find the proportional allocation for the valuation
        :return: the envy free allocation

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
        this function get a consumption graph and use cvxpy to solve
        the convex problem to find a proportional allocation.
        the condition for the convex problem is:
        1) each alloc[i][j] >=0 - an agent cant get minus pesent
        from some item
        2) if consumption_graph[i][j] == 0 so alloc[i][j]= 0 .
        if in the current consumption graph the agent i doesnt consume the item j
        so in the allocation he is get 0% from this item
        3) the proportional condition (by definition)
        4) the sum of every column in the allocation == 1
        each item divided exactly to 100 percent
        and after solving the problem - check if the result are better from the
        "min_sharing_allocation"  (meaning if the current allocation as lass shering from "min_sharing_allocation")
        and update it
        :param consumption_graph: some given consumption graph
        :return: update "min_sharing_allocation"
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
            constraints.append(count >= sum(self.valuation[i]) / len(self.valuation))
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
