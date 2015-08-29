import networkx as nx
import numpy as np

def triangles(G,nodes=None):
    if G.is_multigraph():
        raise NetworkXError("Not defined for multigraphs.")

    nodes_nbrs = G.adj.items()

    n1,n2,n3,n4 = 0,0,0,0

    for v,v_nbrs in nodes_nbrs:
        for w in v_nbrs:
            ws = set(G[w])
            n1+=len(vs.intersection(ws))
    return n1 / (2 * G.number_of_nodes())

def tri(G):
  n1,n2,n3,n4 = 0,0,0,0
  for i in G.edges_iter():
    intersections = list(set(G[i[0]]).intersection(set(G[i[1]])))
    for j in intersections:
      sign = G[i[0]][i[1]]['weight'] * G[i[0]][j]['weight'] * G[i[1]][j]['weight']
      print sign
    n1 += len(set(G[i[0]]).intersection(set(G[i[1]])))
  return n1/3

adj = np.array([[ 0.,  0.,  1.,  1.],
       [ 0.,  0.,  1.,  0.],
       [ 1.,  1.,  0., -1.],
       [ 1.,  0., -1.,  0.]])

G = nx.from_numpy_matrix(adj)

print tri(G)
