import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add some nodes
nodes = range(1, 6)
G.add_nodes_from(nodes)

# Add some edges
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
G.add_edges_from(edges)

# Position nodes in a grid-like pattern
positions = {1: (1, 1), 2: (1, 2), 3: (2, 1), 4: (2, 2), 5: (3, 1)}

# Set the dimensions
width = 4  # assuming you want a width that spans from 0 to 4
height = 3  # assuming you want a height that spans from 0 to 3

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')

# Configure and show grid
plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Setting axis labels and ticks
plt.xlabel('Width')
plt.ylabel('Height')
plt.xticks(range(0, width+1))  # Set ticks for x-axis based on width
plt.yticks(range(0, height+1))  # Set ticks for y-axis based on height

plt.title('Simple Graph on a Grid with Labeled Axes')
plt.show()
