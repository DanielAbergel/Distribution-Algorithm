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
        self.__is_prop = True
        self.__calculate_prop = False
        self.__num_of_sharing = -1

    def get_graph(self):
        return self.__graph

    def get_num_of_sharing(self) -> int:
        """
        this function return the number of
        sharing in the ConsumptionGraph
        and calculate it only one time
        >>> g = ConsumptionGraph([[1, 1, 0.0], [0.0, 1, 1], [0.0, 0.0, 0.0]])
        >>> g.get_num_of_sharing()
        1.0
        >>> g.get_num_of_sharing()
        1.0
        >>> g = ConsumptionGraph([[1, 1, 1], [0.0, 1, 1], [1, 0.0, 0.0]])
        >>> g.get_num_of_sharing()
        3.0
        >>> g = ConsumptionGraph([[0.0, 0.0, 1], [0.0, 1, 0.0], [1, 0.0, 0.0]])
        >>> g.get_num_of_sharing()
        0.0
        >>> g = ConsumptionGraph([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        >>> g.get_num_of_sharing()
        0.0
        >>> g = ConsumptionGraph([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]])
        >>> g.get_num_of_sharing()
        4.0
        """
        if self.__num_of_sharing == -1:
             num_of_edge = 0
             for i in range(len(self.__graph)):
                 num_of_edge += sum(self.__graph[i])
             num_of_obj = len(self.__graph[0])
             if(num_of_edge - num_of_obj < 0 ):
                    self.__num_of_sharing =  0.0
             else:
                self.__num_of_sharing = num_of_edge - num_of_obj
        return self.__num_of_sharing

    def is_prop(self,valuation_matrix) -> bool:
        """
        this function return if this graph is
        not proportional
        note - is this phase we can only know if from this graph
        you cant make a prop  allocation
        this function calculate like every agent gets all the objects he is connecting to.
        (and calculate it only one time)
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g = ConsumptionGraph([[0,0,1,1],[1,1,0,1]])
        >>> g.is_prop(v)
        True
        >>> v = [[11,3],[7,7]]
        >>> g = ConsumptionGraph([[0,1],[1,0]])
        >>> g.is_prop(v)
        False
        >>> v = [[11,3],[7,7]]
        >>> g = ConsumptionGraph([[1,0],[0,1]])
        >>> g.is_prop(v)
        True
        >>> v = [[11,3],[7,7],[3,6]]
        >>> g = ConsumptionGraph([[0,0],[0,1],[1,1]])
        >>> g.is_prop(v)
        False
        """
        if self.__calculate_prop == False:
            self.__calculate_prop == True
            flag = True
            i = 0
            while(i < len(self.__graph))and(flag):
                if not (self.is_single_proportional(valuation_matrix, i)):
                    flag = False
                    self.__is_prop = False
                i += 1
        return self.__is_prop


    def is_single_proportional(self, matv, x):
        """
        this function check if the ConsumptionGraph is proportional
        according to single agent i
        for specific i and any j : ui(xi)>=1/n(xi)
        :param matv represent the value for the agents
        :param x the index of agent we check
        :return: bool value if the allocation is proportional
        >>> g = ConsumptionGraph([[1,1,0,0],[1,1,0,1]])
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g.is_single_proportional(v,0)
        False
        >>> g.is_single_proportional(v,1)
        True
        >>> g = ConsumptionGraph([[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 0.0, 0.0]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        False
        >>> g.is_single_proportional(v,1)
        True
        >>> g.is_single_proportional(v,2)
        False
        >>> g = ConsumptionGraph([[1, 1, 1], [0.0, 1, 1], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        True
        >>> g.is_single_proportional(v,1)
        True
        >>> g.is_single_proportional(v,2)
        False
        >>> g = ConsumptionGraph([[0.0, 0.0, 1], [0.0, 1, 0.0], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,1,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        True
        >>> g.is_single_proportional(v,1)
        False
        >>> g.is_single_proportional(v,2)
        False
        """
        sum = 0
        part = 0
        for i in range(0, len(self.__graph[0])):
            sum += matv[x][i]
            part += matv[x][i] * self.__graph[x][i]
        sum = sum / len(matv)
        return part >= sum

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

