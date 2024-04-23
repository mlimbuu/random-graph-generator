import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import json
import time
'''

1) Nodes Initialization: The graph starts with n nodes.
2) Columns and Rows Initialization: The graph is a 2D grid graph with rows and columns.
'''

## moderate: 2D grid graph, grid connections
def create_moderate_grid_graph(rows, cols):
    # Create a 2D grid graph
    G = nx.grid_2d_graph(rows, cols)
    # Convert node labels from (x,y) to a continuous range of integers
    G = nx.convert_node_labels_to_integers(G)
    return G

def plot_graph(G):
    # Using nx.spring_layout for positioning nodes, with the incremented graph
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
    title = f"grid_style_N{N}_{rows}x{cols}"
    plt.title(title)
    # Save the plot
    plt.savefig(f'./random_graph_generator/grid_style/plots/{title}.png')
    # Show the plot
    plt.show()

# Example usage
# Grid: 2x5, 10 nodes, node labels: 1 - 10
# Grid: 3x5, 15 nodes, node labels: 1 - 15
# Grid: 4x5, 20 nodes, node labels: 1 - 20
# Grid: 5x5, 25 nodes, node labels: 1 - 25
# Grid: 6x5, 30 nodes, node labels: 1 - 30
N = 15 # Number of nodes
cols = 5 # Number of columns
rows, cols = N//cols, cols


grid_graph = create_moderate_grid_graph(rows, cols)
print(f"grid_graph: {grid_graph}")
plot_graph(grid_graph)
