
import networkx as nx
import math as math
import doctest


if __name__ == '__main__':
    (failures,tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures,tests))

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
    Check if the given graph contains a cycle in which the sum of weights is negative.
    :param digraph: a networkx directed graph object.
    :return: True of the graph contains a directed cycle with negative sum of weights; False otherwise.

    >>> q = nx.DiGraph()
    >>> q.add_edge('a', 'b', weight=0.5)
    >>> q.add_edge('b', 'c', weight=0.3)
    >>> q.add_edge('c', 'a', weight=0.4)
    >>> has_cyc_less_than_one(q)
    False

    >>> q['c']['a']['weight'] =0.1
    >>> has_cyc_less_than_one(q)
    True
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