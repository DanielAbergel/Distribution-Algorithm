import doctest as doctest
import itertools
import numpy as np
import math


def graph_code(graph):
    """
    this function generate all the graph_code
    :param graph: graph that represent all agent and there properties
    :return: generator to all the cartesian product that represent all the graph code
    >>> a =[[1,0,0],[1,1,1],[1,1,0]]
    >>> for x in graph_code(a):
    ...     print(x)
    (0, 0, 0)
    (0, 0, 1)
    (0, 1, 0)
    (0, 1, 1)
    (0, 2, 0)
    (0, 2, 1)
    >>> a =[[1,1,0,0],[1,1,1,1],[1,1,0,0]]
    >>> for x in graph_code(a):
    ...     print(x)
    (0, 0, 0)
    (0, 0, 1)
    (0, 1, 0)
    (0, 1, 1)
    (0, 2, 0)
    (0, 2, 1)
    (0, 3, 0)
    (0, 3, 1)
    (1, 0, 0)
    (1, 0, 1)
    (1, 1, 0)
    (1, 1, 1)
    (1, 2, 0)
    (1, 2, 1)
    (1, 3, 0)
    (1, 3, 1)
    """
    agent_prop_counter = sum_of_agent_prop(graph)
    for element in itertools.product(*(range(x) for x in agent_prop_counter)):
        yield element


def sum_of_agent_prop(graph):
    """
    this function return array that each arr[i] = the number
    of properties of agent i in graph
    :param graph:  given graph
    :return:  the number of properties of each agent in array
    >>> a =[[1,0,0],[1,1,1],[1,1,0]]
    >>> sum_of_agent_prop(a)
    [2, 6, 4]
    >>> a =[[1,1,0],[1,1,1]]
    >>> sum_of_agent_prop(a)
    [4, 6]
    >>> a =[[1,0,0],[1,1,1],[1,1,0]]
    >>> sum_of_agent_prop(a)
    [2, 6, 4]
    >>> a =[[1,0,0],[0,0,1],[0,0,0]]
    >>> sum_of_agent_prop(a)
    [2, 2, 0]
    """
    num_of_agent = len(graph)
    agent_prop_counter =[0]*num_of_agent
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if(graph[i][j] == 1):
                agent_prop_counter[i] += 1
    agent_prop_counter= [i * 2 for i in agent_prop_counter]
    return agent_prop_counter





def all_graph(matv):
    pass
def add_agent(matv,gen,i):
    pass
def add_agent_to_graph(matv, graph,i):
    pass



def code_to_matrix(matv,graph,code):
    """
    this function take code and that represent new graph and convert
    it to that graph (represent in matrix)
    the calculation of the properties of each agent is p[i]/2 from the end of arr belongs to the new agent
    and len(arr)-p[i]/2 from the start of arr belongs to agent i
    :param matv: the values of the agent to the objects
    :param graph: the original graph (represent in matrix)
    :param code: the code in form (x1,x2...xi) i = the number of agent in graph, xi in range(number of properties of
    agent i in graph
    :return: matrix that represent the new graph

    """
    mat = np.zeros((len(graph)+1,len(graph[0]))).tolist()
    for i in range(len(graph)):
        arr = build_the_value_ratio_array(matv,graph,i,len(graph))
        num_of_prop = len(arr)
        current_agent_properties = math.ceil(num_of_prop - code[i]/2)
        new_agenrt_properties =  math.ceil(code[i]/2)
        for j in range(current_agent_properties):
            mat[i][arr[j][0]] = 1
        for j in range(num_of_prop - new_agenrt_properties, num_of_prop):
            mat[len(graph)][int(arr[j][0])] = 1
    return mat


def takeSecond(elem):
    return elem[1]

def build_the_value_ratio_array(matv,graph,x, y):
    """
    this function build the array for value ratio between agent x to agent y
    according to the given graph and the properties of agent x in this graph
    and sort it
    :param matv:  represent- the Agents value for the objects
    :param graph: the current graph we working on
    :param x: the index of the first agent
    :param y: the index of the second agent
    :return: the sorted array of tuples (index of location in v, the ratio)
    >>> g = [[1,1,1,1]]
    >>> a = [[20,30,40,10],[10,60,10,20]]
    >>> build_the_value_ratio_array(a,g,0,1)
    [(2, 4.0), (0, 2.0), (1, 0.5), (3, 0.5)]
    >>> g = [[0.0,1,0.0,1]]
    >>> a = [[20,30,40,10],[10,60,10,20]]
    >>> build_the_value_ratio_array(a,g,0,1)
    [(1, 0.5), (3, 0.5)]

    """
    n = len(matv[0])
    l = []
    for i in range(0,n):
        if(graph[x][i]==1):
            try:
                temp = matv[x][i]/matv[y][i]
            except ZeroDivisionError:
                temp = float('Inf')
            l.append((i,temp))
    l.sort(key=takeSecond , reverse=True)
    return l


if __name__ == '__main__':
    a = [[40,30,20],[40,30,20],[10,10,10]]
    b = [[1,1,0],[0,1,1]]
    c =(2,4)
    #print(build_the_value_ratio_array(a,b,1,2))
    print(code_to_matrix(a,b,c))
    #(failures, tests) = doctest.testmod(report=True)
    #print("{} failures, {} tests".format(failures, tests))



