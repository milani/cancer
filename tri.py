import networkx as nx
import numpy as np

def tri(G):
    n1,n2,n3,n4 = 0,0,0,0
    n5 = 0
    for i in G.edges_iter():
        intersections = list(set(G[i[0]]).intersection(set(G[i[1]])))
        n5+=len(intersections)
        for j in intersections:
            if G[i[0]][i[1]]['weight'] > 0 and G[i[0]][j]['weight'] > 0 and G[i[1]][j]['weight'] > 0:
                n1+=1
            elif G[i[0]][i[1]]['weight'] < 0 and G[i[0]][j]['weight'] < 0 and G[i[1]][j]['weight'] < 0:
                n4+=1
            elif G[i[0]][i[1]]['weight'] * G[i[0]][j]['weight'] * G[i[1]][j]['weight'] < 0:
                n2+=1
            elif G[i[0]][i[1]]['weight'] * G[i[0]][j]['weight'] * G[i[1]][j]['weight'] > 0:
                n3+=1
    return n1/3,n2/3,n3/3,n4/3,n5/3


adj = np.array([[ 0.,  0.,  0.4,  1.],
                [ 0.,  0.,    1.,  0.],
                [ 0.4,  1.,  0., 1.],
                [   1.,  0., 1.,  0.]])

G = nx.from_numpy_matrix(adj)

print tri(G)
