import doctest as doctest
import cvxpy
from algorithm.Version1.GraphGenerator import generate_all_consumption_graphs
import colorama
import math

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



def number_of_sharing(graph)->int:
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


def find_envy_free_alloction_for_graph(consumption_graph, matv):
    """

    :param consumption_graph:
    :param matv:
    :return:
    """
    mat = cvxpy.Variable((len(consumption_graph), len(consumption_graph[0])))
    constraints = []
    # every var >=0 and if there is no edge the var is zero
    for i in range(len(consumption_graph)):
        for j in range(len(consumption_graph[0])):
            if (consumption_graph[i][j] == 0):
                constraints.append(mat[i][j] == 0)
            else:
                constraints.append(mat[i][j] >= 0)
    # the sum of each column is 1 (the property on each object is 100%)
    for i in range(len(consumption_graph[0])):
        constraints.append(sum(mat[:, i]) == 1)

    # the envy_free condition
    for i in range(len(consumption_graph)):
        agent_sum = 0
        for j in range(len(consumption_graph[i])):
            agent_sum += mat[i][j] * matv[i][j]
        anther_agent_sum = 0
        for j in range(len(consumption_graph)):
            anther_agent_sum = 0
            for k in range(len(consumption_graph[i])):
                anther_agent_sum += mat[j][k] * matv[i][k]
            constraints.append(agent_sum >= anther_agent_sum)

    objective = cvxpy.Maximize(1)
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()  # Returns the optimal value.
        #print("status:", prob.status)
        #print("optimal value", prob.value)
        #print("optimal var", mat.value)
    g = mat.value
    if not (prob.status == 'infeasible'):
       for i in range(len(g)):
           for j in range(len(g[i])):
               g[i][j] = (int)(g[i][j] * 1000)
               g[i][j] = g[i][j] / 1000
    #check_result_find_proprtional_alloction(prob, g, consumption_graph, matv)
    #check_result_find_envy_free_alloction_for_graph(prob, g, consumption_graph, matv)
    return g


def find_proprtional_alloction_for_graph(consumption_graph, matv):
    """

    :param consumption_graph:
    :param matv:
    :return:
    """
    mat = cvxpy.Variable((len(consumption_graph), len(consumption_graph[0])))
    constraints = []

    # every var >=0 and if there is no edge the var is zero
    for i in range(len(consumption_graph)):
        for j in range(len(consumption_graph[0])):
            if (consumption_graph[i][j] == 0):
                constraints.append(mat[i][j] == 0)
            else:
                constraints.append(mat[i][j] >= 0)

    # the sum of each column is 1 (the property on each object is 100%)
    for i in range(len(consumption_graph[0])):
        constraints.append(sum(mat[:, i]) == 1)

    # the proportional condition
    count = 0
    for i in range(len(consumption_graph)):
        count = 0
        for j in range(len(consumption_graph[i])):
            count += mat[i][j] * matv[i][j]
        constraints.append(count >= sum(matv[i]) / len(matv[i]))

    objective = cvxpy.Maximize(1)
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()  # Returns the optimal value.
    if not (prob.status == 'infeasible'):
        pass
        #print("status:", prob.status)
        #print("optimal value", prob.value)
        #print("optimal var", mat.value)
    g = mat.value
    #check_result_find_proprtional_alloction_for_graph(prob, g, consumption_graph, matv)
    return g




def check_result_find_proprtional_alloction_for_graph(prob, g, graph, matv):
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
        for i in range(len(g)):
            for j in range(len(g[i])):
                g[i][j] = (int)(g[i][j] * 1000)
                g[i][j] = g[i][j] / 1000
        # check if the column sum is 1
        for i in range(len(g)):
            if(sum(g[:, i])>1.00001)and(sum(g[:, i])<0.9999999999999998):
                print(colorama.Fore.RED + "bug 0!!!" + colorama.Fore.RESET)
            #print("the colum sum number {} is :{}".format(i,sum(g[:, i])))

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
            if(agent_sum - n < -0.01):

                print(colorama.Fore.RED +"bug 3!!! in agent {} the difference is : {}".format(i,agent_sum - n)+ colorama.Fore.RESET)



def check_result_find_envy_free_alloction_for_graph(prob, g, graph, matv):
    """
    this function check the result of the function graph_convex
    bug 0 = if the sum of column isnt == 1
    bug 1 = if one of the alloction is greater than one
    bug 2 = if there is no edge in the original graph and the alloc is not zero
    bug 3 = if the alloc for agent i is < 1/n (proportional)
    bug 4 = if the alloc for agent i is < anther agent according to i valuation (envy free)
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
            #print("the colum sum number {} is :{}".format(i,sum(g[:, i])))

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
            #if(agent_sum - n < -0.0001):
            if (agent_sum - n < 0):
                print(colorama.Fore.RED +"bug 3!!! in agent {} the difference is : {}".format(i,agent_sum - n)+ colorama.Fore.RESET)
        temp = g
        # check envy-free
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                temp[i][j] = (int)(temp[i][j] * 1000)
                temp[i][j] = temp[i][j] / 1000
        #print(temp)
        for i in range(len(graph)):
            agent_sum = 0
            for j in range(len(graph[i])):
                agent_sum += g[i][j] * matv[i][j]
            for j in range(len(graph)):
                anther_agent_sum = 0
                for k in range(len(graph[i])):
                    anther_agent_sum += g[j][k] * matv[i][k]
                if not (agent_sum - anther_agent_sum > -0.0001):
                    print(colorama.Fore.RED +"bug 4 !!! in agent {} , his sum is {} ,and agent {} sum is {} the difference is : {}".format(i,agent_sum,j, anther_agent_sum, agent_sum - anther_agent_sum)+ colorama.Fore.RESET)




def num_of_shering2(graph):
    """

    :param graph:
    :return:
    >>> g = [[0.    ,0.    ,0.    ,1.   ],[0.    ,0.329 ,1.    ,0.   ],[1.    ,0.67  ,0.    ,0.   ]]
    >>> num_of_shering2(g)
    1
    >>> g = [[0.   , 0.    ,0.    ,0.977],[0.    ,0.305 ,1.    ,0.022],[1.    ,0.694 ,0.    ,0.   ]]
    >>> num_of_shering2(g)
    2
    """
    num_of_edge = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            num_of_edge += math.ceil(graph[i][j])
    num_of_obj = len(graph[0])
    return num_of_edge - num_of_obj


def find_alloction(matv):
    n = len(matv)+1
    ans = matv
    for i in generate_all_consumption_graphs(matv):
        temp = find_envy_free_alloction_for_graph(i, matv)
        if (temp is not None):
            tempn = num_of_shering2(temp)
            if(tempn < n):
                n = tempn
                ans = temp
    return ans

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

    v = [[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6]]
    g = find_alloction(v)
    print("the ans is: ")
    print(g)
    """
    
    for i in generate_all_consumption_graphs(v):
        print()
        print()
        print(i)
        g = find_envy_free_alloction_for_graph(i, v)
        #g = find_proprtional_alloction(i, v)
        print(g)
        print()
        print()
        print()
    """
