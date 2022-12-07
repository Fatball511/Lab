#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:03:01 2022

@author: keithcheng
"""
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)


G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from(H.edges)


positions=nx.spring_layout(G)
nx.draw(G,pos=positions)
nx.draw_networkx_labels(G,pos=positions)
plt.draw() 
#%%
G.clear()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

positions=nx.spring_layout(G)
nx.draw(G,pos=positions)
nx.draw_networkx_labels(G,pos=positions)
plt.draw() 

print(G.number_of_nodes())
#%%
#DIY Exercise -1
G.clear()
G.add_nodes_from("ABCDEFGH")
G.add_edges_from([("A","B"),("A","C"),("B","C"),
                  ("C","E"),("C","D"),("D","F"),
                  ("F","G"),("F","H")])
print('degree centrality:',nx.degree_centrality(G))
print('betweenness centrality:',nx.betweenness_centrality(G))

positions=nx.spring_layout(G)
nx.draw(G,pos=positions)
nx.draw_networkx_labels(G,pos=positions)
plt.draw() 
#%%
coauthorshipG=nx.read_graphml("netScience.graphml.xml")

nx.number_connected_components(coauthorshipG)
# Find connected components and convert it into list
listG = list(nx.connected_components(coauthorshipG))
# Find the number of connected components
len(listG)
#%%
Largest_c = max(listG, key=len)
LargC = nx.biconnected_components(coauthorshipG)
#nx.connected_component_subgraphs(coauthorshipG)
len(LargC)
#%%
positions = nx.spring_layout(coauthorshipG)
nx.draw(coauthorshipG,pos=positions)
#%%
positions = nx.spring_layout(Largest_c)
#%%









#%%
