# encoding=utf-8

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as apxa
print nx

G = nx.Graph()
# 建立一个空的无向图
G.add_node(6)
# 添加一个节点1
G.add_edges_from([(1,2),(1,3)])
G.add_edge(2,3)
# 添加一条边2-3（隐含着添加了两个节点2、3）
G.add_weighted_edges_from([(1,6,14.0),(1,3,9.0),(1,2,7.0),(2,3,10.0),(3,6,2.0),(2,4,15.0),(3,4,11.0),(4,5,6.0),(5,6,9.0),])
# edge加权
path = nx.all_pairs_shortest_path(G)

Path_1 = nx.all_pairs_shortest_path(G)

# edges = nx.traversal.bfs_edges(G)
# tree = nx.traversal.bfs_tree(G)



print G.nodes()
# 输出全部的节点： [1, 2, 3]
print G.edges()
# 输出全部的边：[(2, 3)]
print G.number_of_edges()
# 输出边的数量：1
print G.get_edge_data(1,2)
# 输出edge的权重
# 输出节点0、2之间的最短路径序列
print path[1][4]
print Path_1[1][4]
# print tree

# 输出节点0、2之间的最短路径序列

# BFS(Breadth First Search)/DFS(Depth First Search)

print "节点的个数:",G.number_of_nodes()
print "边的条数:",G.number_of_edges()
print "节点1的邻居节点为",G.neighbors(1)
print nx.all_pairs_shortest_path(G)

nx.draw(G)
plt.savefig("Networkfortest.png")
plt.show()

print apxa.min_weighted_vertex_cover(G)