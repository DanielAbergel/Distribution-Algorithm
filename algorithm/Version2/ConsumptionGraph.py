import itertools



class ConsumptionGraph():
    """
    this class represent a graph of consumption of the agents
    represent by binary matrix - if graph[i][j] = 1 its mean that agent i
    consumption the j object
    """

    def __init__(self, graph):
        self.__graph = graph

    def get_graph(self):
        return self.graph

    def num_of_sharing(self) -> int:
        """
        need to check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        this function return the number of
        sharing in the ConsumptionGraph
        """
        num_of_edge = 0
        for i in range(len(self.__graph)):
            num_of_edge += sum(self.__graph[i])
        num_of_obj = len(self.__graph[0])
        return num_of_edge - num_of_obj


    def generate_all_code(self):
        """
        need to check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        this function generate all the codes for that graph
        (the code represent the new graph that can built from this graph and adding new agent)
        :return: generator for all the codes
        """
        agent_prop_counter = self.sum_of_agent_prop(self.graph)
        for element in itertools.product(*(range(x) for x in agent_prop_counter)):
            yield element


    def __sum_of_agent_properties(self):
        """
        need to check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        this function return array that each arr[i] = the number
        of properties of agent i in graph multiple by 2 plus 1
        :param graph:  given graph
        :return:  the number of properties of each agent in array
        """
        num_of_agent = len(self.graph)
        agent_prop_counter = [0] * num_of_agent
        for i in range(len(self.graph)):
            # agent_prop_counter[i] = f(sum(graph[i]))
            for j in range(len(self.graph[0])):
                if (self.graph[i][j] == 1):
                    agent_prop_counter[i] += 1
        agent_prop_counter = [i * 2 + 1 for i in agent_prop_counter]
        return agent_prop_counter