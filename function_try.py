import networkx as nx

def negative_cyc(digraph, start="USD"):
    nodes=list(digraph.node)
    for x in nodes:
       #print( x )
       try:
          path = nx.bellman_ford_path(digraph, start,x)
       except:
           print("there is negative cyc")
           return False
    print("no negative cyc")
    return True
#except NetworkXUnbounded:



def reduction(digraph):
    g= nx.DiGraph()
    for (u, v, d) in G.edges(data=True):
       print(d)
       #g.add_edge(u, v, d['weight'])
       g.add_edge(u,v,math.log(d['weight'],2) )




def test1():
    G = nx.DiGraph()
    G.add_edge('a', 'b', weight=0.6)
    G.add_edge('a', 'c', weight=0.2)
    G.add_edge('c', 'd', weight=0.1)
    G.add_edge('c', 'e', weight=0.7)
    G.add_edge('c', 'f', weight=-0.9)
    G.add_edge('a', 'd', weight=0.3)
    G.add_edge('f', 'a', weight=0.3)
    reduction(G)
    print(negative_cyc(G,'a'))

test1()