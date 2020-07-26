import doctest
from algorithm.Version3.ConsumptionGraph import ConsumptionGraph
from algorithm.Version3.ValueRatio import ValueRatio
import numpy as np
import math


class GraphGenerator():
    """
    this class functionality is to generate all the possibilities graph
    (represent as ConsumptionGraph) for some valuation_matrix
    """

    def __init__(self, valuation_matrix):
        self.valuation_matrix = valuation_matrix
        self.valuation_ratios = ValueRatio(valuation_matrix)
        self.num_of_sharing_is_allowed = len(valuation_matrix)

    def set_num_of_sharing_is_allowed(self , n):
        self.num_of_sharing_is_allowed = n


    def generate_all_consumption_graph(self):
        """
        this is the main function in that part of the algorithm
        she get valuation  and generate all the possibilities graph for it
        represent as ConsumptionGraph
        :return: generator of all possibilities graph
        >>> v = [[20,10],[5,4]]
        >>> gg = GraphGenerator(v)
        >>> for g in gg.generate_all_consumption_graph():
        ...      print(g.get_graph())
        [[1, 0.0], [1, 1]]
        >>> v = [[30,20,10],[5,5,5]]
        >>> gg = GraphGenerator(v)
        >>> for g in gg.generate_all_consumption_graph():
        ...      print(g.get_graph())
        [[1, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [1, 1, 1]]
        >>> v = [[30,20,10],[20,15,10],[5,5,5]]
        >>> gg = GraphGenerator(v)
        >>> # its the same check as ver1 and its work the same (111 count)
        >>> # it spouse to be 101 graphs i didnt check the correctness of the graphs
        >>> for g in gg.generate_all_consumption_graph():
        ...      print(g.get_graph())
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 0.0, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 0.0, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 1, 0.0]]
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 1, 0.0]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 1, 0.0]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 0.0, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 0.0, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 0.0, 0.0]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 0.0, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 0.0, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [1, 1, 1], [0.0, 0.0, 1]]
        [[1, 0.0, 0.0], [1, 1, 0.0], [0.0, 0.0, 1]]
        [[1, 0.0, 0.0], [1, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [1, 0.0, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [1, 0.0, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [1, 1, 1], [1, 0.0, 0.0]]
        [[1, 0.0, 0.0], [1, 1, 1], [1, 0.0, 1]]
        [[1, 0.0, 0.0], [1, 1, 0.0], [1, 0.0, 1]]
        [[1, 0.0, 0.0], [1, 1, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [1, 0.0, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [1, 0.0, 0.0], [1, 1, 1]]
        """
        a = (0)
        genenretor = self.add_agent(a, 0)
        for i in range(1, len(self.valuation_matrix) - 1):
            temp_generator = self.add_agent(genenretor, i)
            genenretor = temp_generator
        for i in genenretor:
            for j in self.add_agent_to_graph(i):
                yield j

    def add_agent(self,genneretor,i):
        """
        this function get generator for all the the graph for i-1 agent
        and generate all the graph for adding agent i
        :param genneretor: generator for the all the  graph for i-1 agents
        :param i: the index for the new agent
        :return: generator for the all the  graph for i agents
        >>> a = (0)
        >>> matv = [[30,20,10],[20,15,10],[5,5,5]]
        >>> gg = GraphGenerator(matv)
        >>> gen = gg.add_agent(a,0)
        >>> for g in gg.add_agent(gen,1):
        ...       print(g.get_graph())
        [[1, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [1, 1, 1]]
        """
        if (i == 0):
            arr = []
            # the first agent gets all the objects
            arr.append([1] * len(self.valuation_matrix[0]))
            yield ConsumptionGraph(arr)
        else:
            for g in genneretor:
                for x in self.add_agent_to_graph(g):
                    yield x

    def add_agent_to_graph(self, consumption_graph: ConsumptionGraph):
        """
        :param consumption_graph: : some given ConsumptionGraph that represent agent and there properties
        :return: generator for the all the  graphs from adding agent i to the given graph
        >>> matv = [[40,30,20],[40,30,20],[10,10,10]]
        >>> graph = [[1,1,0],[0,1,1]]
        >>> g = GraphGenerator(matv)
        >>> cg = ConsumptionGraph(graph)
        >>> for x in g.add_agent_to_graph(cg):
        ...     print(x.get_graph())
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 0.0, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 0.0, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 1, 0.0]]
        [[1, 1, 0.0], [0.0, 1, 1], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 1, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 1, 0.0]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [0.0, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 1, 0.0]]
        [[1, 0.0, 0.0], [0.0, 1, 1], [1, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 1, 1]]
        [[1, 0.0, 0.0], [0.0, 1, 0.0], [1, 1, 1]]
        >>> matv = [[40,30,20],[40,30,20],[10,10,10]]
        >>> graph = [[1,1,1],[0,0,0]]
        >>> g = GraphGenerator(matv)
        >>> cg = ConsumptionGraph(graph)
        >>> for x in g.add_agent_to_graph(cg):
        ...     print(x.get_graph())
        """
        for code in consumption_graph.generate_all_code():
            g = self.code_to_consumption_graph(consumption_graph, code)
            #anther adding!!!
            if(g.is_prop(self.valuation_matrix))and(g.get_num_of_sharing() <= self.num_of_sharing_is_allowed):
            # the fixing!!
            #if (g.get_num_of_sharing() <= self.num_of_sharing_is_allowed):
                    yield g

    def code_to_consumption_graph(self, consumption_graph: ConsumptionGraph, code) -> ConsumptionGraph:
        """
        this function take code that represent new graph and convert
        it to that consumption_graph
        the calculation of the properties of each agent is p[i]/2 from the end of arr belongs to the new agent
        and len(arr)-p[i]/2 from the start of arr belongs to agent i
        :param consumption_graph: the original graph
        :param code:the code in form (x1,x2...xi) i = the number of agent in graph, xi in range(number of properties of
         agent i in graph
        :return: consumption_graph for that code
        >>> v = [[40,30,20,10],[40,30,20,10],[40,30,20,10],[10,10,10,10]]
        >>> gg = GraphGenerator(v)
        >>> g = [[0,1,1,0],[1,0,0,0],[0,1,0,1]]
        >>> cg = ConsumptionGraph(g)
        >>> print(gg.code_to_consumption_graph(cg,(0,0,0)).get_graph())
        [[0.0, 1, 1, 0.0], [1, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 1], [0.0, 0.0, 0.0, 0.0]]
        >>> print(gg.code_to_consumption_graph(cg,(4,1,3)).get_graph())
        [[0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 0.0], [1, 1, 1, 1]]
        >>> v1 = [[1,2,3,4],[8,7,6,5],[9,12,10,11],[1,2,3,4]]
        >>> g1 = [[0,1,1,0],[1,0,0,0],[0,1,0,1]]
        >>> gg = GraphGenerator(v1)
        >>> cg = ConsumptionGraph(g1)
        >>> print(gg.code_to_consumption_graph(cg,(2,3,2)).get_graph())
        [[0.0, 1, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 0.0], [1, 0.0, 1, 1]]
        >>> print(gg.code_to_consumption_graph(cg,(4,1,3)).get_graph())
        [[0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 0.0], [1, 1, 1, 1]]
        >>> print(gg.code_to_consumption_graph(cg,(3,1,1)).get_graph())
        [[0.0, 1, 0.0, 0.0], [1, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 1], [1, 1, 1, 1]]
        >>> print(gg.code_to_consumption_graph(cg,(1,2,3)).get_graph())
        [[0.0, 1, 1, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 1, 0.0, 0.0], [1, 1, 1, 1]]
        >>> v1 = [[1,2,3,4],[8,7,6,5],[9,12,10,11],[1,4,3,2]]
        >>> gg = GraphGenerator(v1)
        >>> print(gg.code_to_consumption_graph(cg,(2,3,2)).get_graph())
        [[0.0, 0.0, 1, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1], [1, 1, 0.0, 0.0]]
        """
        graph = consumption_graph.get_graph()
        mat = np.zeros((len(graph) + 1, len(graph[0]))).tolist()
        for i in range(len(graph)):
            arr = self.valuation_ratios.create_the_value_ratio_for_2(consumption_graph,i,len(graph))
            num_of_properties = len(arr)
            current_agent_properties = math.ceil(num_of_properties - code[i] / 2)
            new_agent_properties = math.ceil(code[i] / 2)
            for j in range(current_agent_properties):
                mat[i][arr[j][0]] = 1
            for j in range(num_of_properties - new_agent_properties, num_of_properties):
                mat[len(graph)][int(arr[j][0])] = 1
        return ConsumptionGraph(mat)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
