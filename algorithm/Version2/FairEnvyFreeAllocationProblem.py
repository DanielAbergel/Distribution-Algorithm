import doctest
import cvxpy
from algorithm.Version2.Allocation import Allocation
from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.FairAllocationProblem import FairAllocationProblem


class FairEnvyFreeAllocationProblem(FairAllocationProblem):


    def __init__(self, valuation):
        super().__init__(valuation)

    def find_allocation_with_min_shering(self):
        """
        :return:
        # the test are according to the result of ver 1 in GraphCheck
        >>> v = [[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6]]
        >>> fefap =FairEnvyFreeAllocationProblem(v)
        >>> print(fefap.find_allocation_with_min_shering())
        [[0.    0.    0.    1.   ]
         [0.    1.    0.437 0.   ]
         [1.    0.    0.562 0.   ]]
        >>> v = [[5, 2, 1.5,1], [9, 1, 3,2.5], [10, 3, 2,4]]
        >>> fefap =FairEnvyFreeAllocationProblem(v)
        >>> print(fefap.find_allocation_with_min_shering())
        [[0.333 1.    0.    0.   ]
         [0.333 0.    1.    0.   ]
         [0.333 0.    0.    1.   ]]
        """
        for consumption_graph in self.graph_generator.generate_all_consumption_graph():
            self.find_allocation_for_graph(consumption_graph)
        return self.min_sharing_allocation


    def find_allocation_for_graph(self,consumption_graph : ConsumptionGraph):
        """
        :param consumption_graph:
        :return:
        # the test are according to the result of ver 1 in GraphCheck
        >>> v = [[5, 2, 1.5,1], [9, 1, 3,2.5], [10, 3, 2,4]]
        >>> fefap =FairEnvyFreeAllocationProblem(v)
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 0.0], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        [[0.333 1.    0.    0.   ]
         [0.333 0.    1.    0.   ]
         [0.333 0.    0.    1.   ]]
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 0.0], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        [[0.333 1.    0.    0.   ]
         [0.333 0.    1.    0.   ]
         [0.333 0.    0.    1.   ]]
        >>> g1 = [[1, 1, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [1, 0.0, 1, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        None
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 1], [1, 0.0, 0.0, 0.0]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        [[0.299 1.    0.    0.   ]
         [0.047 0.    1.    0.999]
         [0.653 0.    0.    0.   ]]
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 1], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        [[0.329 1.    0.    0.   ]
         [0.224 0.    1.    0.427]
         [0.446 0.    0.    0.572]]
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 1], [0.0, 0.0, 0.0, 0.0]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        None
        >>> g1 = [[1, 1, 0.0, 0.0], [1, 0.0, 1, 0.0], [1, 0.0, 0.0, 1]]
        >>> g = ConsumptionGraph(g1)
        >>> print(fefap.find_allocation_for_graph(g))
        [[0.333 1.    0.    0.   ]
         [0.333 0.    1.    0.   ]
         [0.333 0.    0.    1.   ]]
        """
        mat = cvxpy.Variable((self.num_of_agents, self.num_of_items))
        constraints = []

        # every var >=0 and if there is no edge the var is zero
        # and envy_free condition
        for i in range(self.num_of_agents):
            agent_sum = 0
            for j in range(self.num_of_items):
                agent_sum += mat[i][j] * self.valuation[i][j]
                if (consumption_graph.get_graph()[i][j] == 0):
                    constraints.append(mat[i][j] == 0)
                else:
                    constraints.append(mat[i][j] >= 0)
            anther_agent_sum = 0
            for j in range(self.num_of_agents):
                anther_agent_sum = 0
                for k in range(self.num_of_items):
                    anther_agent_sum += mat[j][k] * self.valuation[i][k]
                constraints.append(agent_sum >= anther_agent_sum)

        # the sum of each column is 1 (the property on each object is 100%)
        for i in range(self.num_of_items):
            constraints.append(sum(mat[:, i]) == 1)

        objective = cvxpy.Maximize(1)
        prob = cvxpy.Problem(objective, constraints)
        prob.solve()  # Returns the optimal value.
        if not (prob.status == 'infeasible'):
            alloc = Allocation(mat.value)
            alloc.round()
            if (alloc.num_of_shering() < self.min_sharing_number):
                self.min_sharing_number = alloc.num_of_shering()
                self.min_sharing_allocation = alloc.get_allocation()
        # only for doctet:
        return (mat.value)

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))