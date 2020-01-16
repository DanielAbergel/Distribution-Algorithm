from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.ValueRatio import ValueRatio
import numpy as np
import  math
class GraphGenerator():

    def __init__(self, valuation_matrix):
        self.valuation_matrix = valuation_matrix
        self.valuation_ratios = ValueRatio(valuation_matrix)


    def generate_all_consumption_graph(self):
        pass

    def __add_agent(self):
        pass

    def __add_agent_to_graph(self):
        pass



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
        (i check this method in all the tests of the ether function from ver1)
        """
        graph = consumption_graph.get_graph()
        mat = np.zeros((len(graph) + 1, len(graph[0]))).tolist()
        for i in range(len(graph)):
            arr = self.valuation_ratios.create_the_value_ratio_for_2(consumption_graph,i,len(graph))
            num_of_properties = len(arr)
            current_agent_properties = math.ceil(num_of_properties - code[i] / 2)
            new_agenrt_properties = math.ceil(code[i] / 2)
            for j in range(current_agent_properties):
                mat[i][arr[j][0]] = 1
            for j in range(num_of_properties - new_agenrt_properties, num_of_properties):
                mat[len(graph)][int(arr[j][0])] = 1
        return ConsumptionGraph(mat)


if __name__ == '__main__':
    pass
