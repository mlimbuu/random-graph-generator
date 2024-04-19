import networkx as nx
import matplotlib.pyplot as plt

'''
1) Nodes Initialization: The graph starts with n nodes.
2) Random Edge Selection: M edges are selected randomly from 
the set of all possible nC2 edges. Each selected edge is unique and
totall number of edges is  exactly M.

Note: For n=10 nodes, there are nC2 = 45 possible edges that can be added.
The total number of edges M is specified by the user and should be less than nC2.
'''

# Parameters
n = 10  # number of nodes
M = 30  # number of edges #15

# Create a random graph using the G(n, M) model
G = nx.gnm_random_graph(n, M)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=700, edge_color='k')
plt.title('Random Graph from G(n, M) Model')
# Save the plot
plt.savefig(f'./random_graph_generator/erdos_renyi/plots/random_graph_gnm_G({n},{M}).png')
# Show the plot
plt.show()
