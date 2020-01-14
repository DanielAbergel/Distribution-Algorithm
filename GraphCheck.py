import doctest as doctest
import cvxpy
import numpy as np
from GraphGenerator import all_graph as all_graph
import colorama


def sum_of_x_according_to_y(graph, matv,x,y):
    """
    this function calculate the sum of the properties
     of agent x according to the valuation of agent y
    :param graph: the allocation represent by matrix
    :param matv: the valuation of the agent represent by matrix
    :param x: the index of the agent we calculate his sum
    :param y: the index of the agent that we calculate according to his valuation
    :return: the sum of the properties of agent x according to the valuation of agent y
    >>> g = [[1,0,0],[1,1,1],[1,1,0]]
    >>> v = [[1,2,3],[4,5,6],[7,8,9]]
    >>> sum_of_x_according_to_y(g,v,0,1)
    4
    >>> sum_of_x_according_to_y(g,v,0,2)
    7
    >>> sum_of_x_according_to_y(g,v,1,1)
    15
    >>> sum_of_x_according_to_y(g,v,1,2)
    24
    >>> sum_of_x_according_to_y(g,v,1,0)
    6
    >>> g = [[0.5,0,0],[0.4,0.7,0],[0.1,0.3,1]]
    >>> sum_of_x_according_to_y(g,v,0,1)
    2.0
    >>> sum_of_x_according_to_y(g,v,0,2)
    3.5
    >>> sum_of_x_according_to_y(g,v,1,1)
    5.1
    >>> sum_of_x_according_to_y(g,v,1,2)
    8.4
    >>> sum_of_x_according_to_y(g,v,1,0)
    1.7999999999999998
    """

    sum = 0
    for i in range(len(graph[x])):
        sum += graph[x][i]*matv[y][i]
    return sum



def number_of_sharing(graph):
    """
    this function
    :param graph: a graph represent by matrix
    :return: the number of sharing in this graph
    >>> g = [[1,0,0],[1,1,1],[1,1,0]]
    >>> number_of_sharing(g)
    3
    """
    num_of_edge = 0
    for i in range(len(graph)):
        num_of_edge += sum(graph[i])
    num_of_obj = len(graph[0])
    return num_of_edge - num_of_obj





def graph_convex(graph, matv):
    mat = cvxpy.Variable((len(graph), len(graph[0])))
    constraints = []

    # every var >=0 and if there is no edge the var is zero
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if (graph[i][j] == 0):
                constraints.append(mat[i][j] == 0)
            else:
                constraints.append(mat[i][j] >= 0)

    # the sum of each column is 1 (the property on each object is 100%)
    for i in range(len(graph[0])):
        constraints.append(sum(mat[:, i]) == 1)

    # the proportional condition
    count = 0
    for i in range(len(graph)):
        count = 0
        for j in range(len(graph[i])):
            count += mat[i][j] * matv[i][j]
        constraints.append(count >= sum(matv[i]) / len(matv[i]))

    objective = cvxpy.Maximize(1)
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()  # Returns the optimal value.
    if not (prob.status == 'infeasible'):
        print("status:", prob.status)
        print("optimal value", prob.value)
        #print("optimal var", mat.value)
    g = mat.value
    check_result(prob,g,graph,matv)
    return g




def check_result(prob, g, graph, matv):
    """
    this function check the result of the function graph_convex
    bug 0 = if the sum of column isnt == 1
    bug 1 = if one of the alloction is greater than one
    bug 2 = if there is no edge in the original graph and the alloc is not zero
    bug 3 = if the alloc for agent i is < 1/n (proportional)
    :param prob:
    :param g:
    :param graph:
    :param matv:
    :return:
    """
    colorama.init()


   # chacking if the sum of column isnt == 1
    if not(prob.status == 'infeasible'):
        # check if the column sum is 1
        for i in range(len(g)):
            if(sum(g[:, i])>1.00001)and(sum(g[:, i])<0.9999999999999998):
                print(colorama.Fore.RED + "bug 0!!!" + colorama.Fore.RESET)
            print("the colum sum number {} is :{}".format(i,sum(g[:, i])))

        # check if there is no edge in the graph if he is get anything
        for i in range(len(g)):
            for j in range(len(g[0])):
                if(g[i][j] > 1.000001):
                    print(colorama.Fore.RED +"bug 1!!!"+ colorama.Fore.RESET)
                if(graph[i][j] == 0):
                    if(g[i][j] > 0.001):
                        print(colorama.Fore.RED +"bug 2!!!"+ colorama.Fore.RESET)

        # check proportional
        for i in range(len(graph)):
            agent_sum = 0
            for j in range(len(graph[i])):
                agent_sum += g[i][j] * matv[i][j]
            n = sum(matv[i]) / len(matv[i])
            if(agent_sum - n < -0.0001):

                print(colorama.Fore.RED +"bug 3!!! in agent {} the difference is : {}".format(i,agent_sum - n)+ colorama.Fore.RESET)



if __name__ == '__main__':
    #(failures, tests) = doctest.testmod(report=True)
    #print("{} failures, {} tests".format(failures, tests))
    v = [[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6]]
    for i in all_graph(v):
        print()
        print()
        print(i)
        g = graph_convex(i,v)
        print(g)
        print()
        print()
        print()

