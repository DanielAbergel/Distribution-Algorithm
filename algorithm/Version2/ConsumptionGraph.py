import itertools
import doctest as doctest


class ConsumptionGraph():
    """
    this class represent a graph of consumption of the agents
    represent by binary matrix - if graph[i][j] = 1 its mean that agent i
    consumption the j object
    """

    def __init__(self, graph):
        self.__graph = graph

    def get_graph(self):
        return self.__graph

    def num_of_sharing(self) -> int:
        """
        this function return the number of
        sharing in the ConsumptionGraph
        >>> g = ConsumptionGraph([[1, 1, 0.0], [0.0, 1, 1], [0.0, 0.0, 0.0]])
        >>> g.num_of_sharing()
        1.0
        >>> g = ConsumptionGraph([[1, 1, 1], [0.0, 1, 1], [1, 0.0, 0.0]])
        >>> g.num_of_sharing()
        3.0
        >>> g = ConsumptionGraph([[0.0, 0.0, 1], [0.0, 1, 0.0], [1, 0.0, 0.0]])
        >>> g.num_of_sharing()
        0.0
        >>> g = ConsumptionGraph([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        >>> g.num_of_sharing()
        0.0
        >>> g = ConsumptionGraph([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]])
        >>> g.num_of_sharing()
        4.0
        """
        num_of_edge = 0
        for i in range(len(self.__graph)):
            num_of_edge += sum(self.__graph[i])
        num_of_obj = len(self.__graph[0])
        if(num_of_edge - num_of_obj < 0 ):
            return 0.0
        return num_of_edge - num_of_obj

    def generate_all_code(self):
        """
        this function generate all the codes for that graph
        (the code represent the new graph that can built from this graph and adding new agent)
        :return: generator for all the codes
        >>> a =[[1,0,1]]
        >>> g = ConsumptionGraph(a)
        >>> for x in g.generate_all_code():
        ...     print(x)
        (0,)
        (1,)
        (2,)
        (3,)
        (4,)
    """
        agent_prop_counter = self.sum_of_agent_properties()
        for element in itertools.product(*(range(x) for x in agent_prop_counter)):
            yield element


    def sum_of_agent_properties(self):
        """
        this function return array that each arr[i] = the number
        of properties of agent i in graph multiple by 2 plus 1
        :return:  the number of properties of each agent in array
        >>> a =[[1,0,0],[1,1,1],[1,1,0]]
        >>> g = ConsumptionGraph(a)
        >>> g.sum_of_agent_properties()
        [3, 7, 5]
        >>> a =[[1,1,0],[1,1,1]]
        >>> g = ConsumptionGraph(a)
        >>> g.sum_of_agent_properties()
        [5, 7]
        >>> a =[[1,0,0],[1,1,1],[1,1,0]]
        >>> g = ConsumptionGraph(a)
        >>> g.sum_of_agent_properties()
        [3, 7, 5]
        >>> a =[[1,0,0],[0,0,1],[0,0,0]]
        >>> g = ConsumptionGraph(a)
        >>> g.sum_of_agent_properties()
        [3, 3, 1]
        >>> a =[[1,1]]
        >>> g = ConsumptionGraph(a)
        >>> g.sum_of_agent_properties()
        [5]
        """
        num_of_agent = len(self.__graph)
        agent_prop_counter = [0] * num_of_agent
        for i in range(len(self.__graph)):
            # agent_prop_counter[i] = f(sum(graph[i]))
            for j in range(len(self.__graph[0])):
                if (self.__graph[i][j] == 1):
                    agent_prop_counter[i] += 1
        agent_prop_counter = [i * 2 + 1 for i in agent_prop_counter]
        return agent_prop_counter


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
