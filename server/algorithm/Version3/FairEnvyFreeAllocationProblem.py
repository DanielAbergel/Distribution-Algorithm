import doctest
import cvxpy
from algorithm.Version2.Allocation import Allocation
from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.FairAllocationProblem import FairAllocationProblem


class FairEnvyFreeAllocationProblem(FairAllocationProblem):
    """
    this class solve Fair Envy Free Allocation Problem
    she is inherited from FairAllocationProblem
    envy free definition:
    V = agents valuation
    X = envy free allocation
    For all i, j:
    Vi(Xi) ≥ Vi(Xj)
    """

    def __init__(self, valuation):
        super().__init__(valuation)

    def find_allocation_with_min_shering(self):
        """
        this function find the envy free allocation for the valuation
        :return: the envy free allocation

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
        this function get a consumption graph and use cvxpy to solve
        the convex problem to find a envy free allocation.
        the condition for the convex problem is:
        1) each alloc[i][j] >=0 - an agent cant get minus pesent
        from some item
        2) if consumption_graph[i][j] == 0 so alloc[i][j]= 0 .
        if in the current consumption graph the agent i doesnt consume the item j
        so in the allocation he is get 0% from this item
        3) the envy free condition (by definition)
        4) the sum of every column in the allocation == 1
        each item divided exactly to 100 percent
        and after solving the problem - check if the result are better from the
        "min_sharing_allocation"  (meaning if the current allocation as lass shering from "min_sharing_allocation")
        and update it
        :param consumption_graph: some given consumption graph
        :return: update "min_sharing_allocation"
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