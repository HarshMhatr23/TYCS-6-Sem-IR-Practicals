import networkx as nx
G = nx.DiGraph()
G.add_edges_from([(1,2),(1,3),(2,3),(3,1)])
pagerank_scores = nx.pagerank(G)
hits_scores = nx.hits(G)
print("Page Rank Scores:",pagerank_scores)
print("Hub Scores:",hits_scores[0])
print("Authority Scores:",hits_scores[1])
