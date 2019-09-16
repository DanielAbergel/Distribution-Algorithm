import networkx as nx

G = nx.Graph()
G.add_edge('a', 'b', weight=-0.6)
G.add_edge('a', 'c', weight=-0.2)
G.add_edge('c', 'd', weight=-0.1)
G.add_edge('c', 'e', weight=-0.7)
G.add_edge('c', 'f', weight=-0.9)
G.add_edge('a', 'd', weight=-0.3)



def find_path(digraph, start="USD",end="USD"):
    try:
        path = nx.bellman_ford_path(digraph, start,end)
        return True
    except:
        return False
#except NetworkXUnbounded:



print(find_path(G,'a','f'))