
import networkx as nx
import math as math
import doctest as doctest
import matplotlib.pyplot as plt
import numpy as np

def has_negative_cyc(digraph):
    """
    Check if the given graph contains a cycle in which the sum of weights is negative.
    :param digraph: a networkx directed graph object.
    :return: True of the graph contains a directed cycle with negative sum of weights; False otherwise.

    >>> G = nx.DiGraph()
    >>> G.add_edge('a', 'b', weight=4)
    >>> G.add_edge('b', 'c', weight=-2)
    >>> G.add_edge('c', 'a', weight=-1)
    >>> has_negative_cyc(G)
    False

    >>> G['c']['a']['weight'] = -3
    >>> has_negative_cyc(G)
    True
    """
    try:
        path= dict(nx.all_pairs_bellman_ford_path_length(digraph))
        #print(path)
        #print("no negative cyc")
        return False

    except nx.exception.NetworkXUnbounded as e:
        #print(e)
        #print("there is negative cyc")
        return True





def has_cyc_less_than_one(digraph):
    """
    Check if the given graph contains a cycle in which the multiplying of weights is less than one.
    :param digraph: a networkx directed graph object.
    :return: True of the graph contains a directed cycle with ess than one multiplying of weights; False otherwise.

    >>> q = nx.DiGraph()
    >>> q.add_edge('a', 'b', weight=0.1)
    >>> q.add_edge('b', 'c', weight=0.1)
    >>> q.add_edge('c', 'a', weight=0.1)
    >>> has_cyc_less_than_one(q)
    True

       >>> q['c']['a']['weight'] = 1
    >>> has_negative_cyc(q)
    False
    >>> q['c']['a']['weight'] = 10
    >>> has_cyc_less_than_one(q)
    True

    >>> q['c']['a']['weight'] = 1000
    >>> has_cyc_less_than_one(q)
    False
    """
    g = nx.DiGraph()
    for (u, v, d) in digraph.edges(data=True):
       #print(d)
       #g.add_edge(u, v, weight=d['weight'])
       g.add_edge(u,v,weight=(math.log(d['weight'],2)))
    return has_negative_cyc(g)
    #for (u, v, d) in g.edges(data=True):
     #  print(d)
    #return g


def num_of_shared_objects(z):
    """
    return the number of object that shared = belong to more then on agent
    :param z :  matrix  that represent - given allocation
    :return:  number of shared objects

    >>> z = [ [1, 0, 0],[0.8, 0.1, 0.1],[0, 1, 0]]
    >>> num_of_shared_objects(z)
    1
    >>> z1 = [[1, 0, 0],[0.8, 0.1, 0.1],[0.2, 0.6, 0.2]]
    >>> num_of_shared_objects(z1)
    2
    """
    count = 0
    for i in range(0, len(z)):
        for j in range(0, len(z[0])):
            if(z[i][j] == 1):
                break
            if (z[i][j] > 0):
                count += 1
                break
    return count


def num_of_sharing(mat):
    """
    return the number of sharing in given allocation
    :param mat matrix that represent - given allocation
    :return:  number of sharing

    >>> z = [ [1, 0, 0],[0.8, 0.1, 0.1],[0, 1, 0]]
    >>> num_of_sharing(z)
    2
    >>> z1 = [[1, 0, 0],[0.8, 0.1, 0.1],[0.2, 0.6, 0.2]]
    >>> num_of_sharing(z1)
    4
    """
    count = 0
    temp = 0
    for i in range(0, len(mat)):

        for j in range(0, len(mat[0])):
            if(mat[i][j] > 0)and(mat[i][j] < 1):
                temp += 1
        if not (temp == 0):
            temp += -1
            count += temp
            temp = 0

    return count
def mat_to_directed_graph(matz , matv):
    """
    convert the z matrix to directed graph
    :param matv:  represent- the Agents value for the objects
    :param matz: represent - given allocation
    :return: directed_graph
    >>> z = [ [1, 0.8, 0],[0, 0.2, 1]]
    >>> v = [ [4, 2.5, 1],[1.25, 2, 5]]
    >>> mat_to_directed_graph(z)
    2
    """
    n = len(matz)
    m = len(matz[0])
    g = nx.DiGraph()
    for i in range(0, n):
        for j in range(0, m):
            if(matz[i][j] > 0):
                if(matv[i][j] <= 0):
                    g.add_edge("i"+str(i), "o"+str(j), weight=(matv[i][j]))
                else:
                    g.add_edge("o"+str(j), "i"+str(i), weight=1/(matv[i][j]))
            if(matz[i][j] < 1):
                if(matv[i][j] > 0):
                    g.add_edge("o"+str(i), "i"+str(j), weight=1/(matv[i][j]))
                else:
                    g.add_edge("i"+str(j), "o"+str(i), weight=(matv[i][j]*-1))
    return g


def mat_to_undirected_graph(matz, matv):
    """
    convert the z matrix to directed graph
    :param matv:  represent- the Agents value for the objects
    :param matz: represent - given allocation
    :return: directed_graph

    """
    n = len(matz)
    m = len(matz[0])
    g = nx.DiGraph()
    for i in range(0, len(matz)):
        for j in range(0, len(matz[0])):
            if(matz[i][j] < 1):
                if(matv[i][j] > 0):
                    g.add_edge("o"+str(i), "i"+str(j), weight=1/(matv[i][j]))
                else:
                    g.add_edge("i"+str(j), "o"+str(i), weight=(matv[i][j]*-1))

    return g

def matrix_transpose(mat):
    """
    this function transpose matrix
    """
    ans = [[row[i] for row in mat]for i in range(len(mat[0]))]
    return ans

def printmat(matrix):
    """
    this function print matrix in her shape
    """
    for row in matrix:
        print(row)

def print_graph(G):
    """
    print the given graph with matplotlib.pyplot
    :param digraph: a networkx directed graph object.
    :return: none

    """
    # the printing of the graph
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 100]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 100]
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Weight
    new_labels = dict(
        map(lambda x: ((x[0], x[1]), str(x[2]['weight'] if x[2]['weight'] <= 3 else "")), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=new_labels)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    #v = [[5, 1], [25, 2], [1, 5]]
    #z = [[1, 0], [0.8, 0.2], [0, 1]]
    #G = mat_to_directed_graph(z, v)
   # print_graph(G)
  #(failures, tests) = doctest.testmod(report=True)
  #print("{} failures, {} tests".format(failures, tests))
    z = [ [1, 0.8, 0],[0, 0.2, 1]]
    v = [ [4, 2.5, 1],[1.25, 2, 5]]
    print_graph(mat_to_directed_graph2(v,z))

"""
def test1():
    G = nx.DiGraph()
    G.add_edge('a', 'b', weight=0.6)
    G.add_edge('b', 'c', weight=0.2)
    G.add_edge('c', 'a', weight=0.1)
    #G.add_edge('c', 'e', weight=0.7)
    #G.add_edge('c', 'f', weight=-0.9)
    #G.add_edge('a', 'd', weight=0.3)
   # G.add_edge('f', 'a', weight=0.3)
    g1 = has_cyc_less_than_one(G)
    print(has_negative_cyc(g1,'a'))

#test1()
"""