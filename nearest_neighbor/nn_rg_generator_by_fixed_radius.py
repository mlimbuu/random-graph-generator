import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from random import randint

'''
Edges formation: 
1. For N nodes, nearest neighbours within P fixed raidus are connected to each node.
3. Isolated nodes are connected to their nearest neighbour.
4. Isolated graph sub-components are connected to the main component.
'''

def check_and_connect_isolates(G, positions):
    isolates = list(nx.isolates(G))
    if isolates:
        print(f"Isolated nodes detected: {isolates}")
        for node in isolates:
            # You might want to connect this node to its nearest neighbor not isolated
            distances = [(neighbor, distance(positions[node], positions[neighbor]))
                         for neighbor in set(G.nodes()) - set(isolates)]
            if distances:
                closest_neighbor = min(distances, key=lambda x: x[1])[0]
                G.add_edge(node, closest_neighbor)
                print(f"Connected isolated node {node} to {closest_neighbor}")
    else:
        print("No isolated nodes detected.")
    return G

def connect_components(G, positions):
    # Find all connected components
    components = list(nx.connected_components(G))
    if len(components) > 1:
        print(f"Graph is not fully connected; it has {len(components)} components.")
        # Sort components by size and connect smallest to largest to minimize added edge length
        components = list(sorted(components, key=len))
        main_component = components[-1]  # Largest component
        for component in components[:-1]:
            # Connect each smaller component to the largest component
            closest_pair = None
            min_distance = float('inf')
            for node in component:
                for main_node in main_component:
                    dist = distance(positions[node], positions[main_node])
                    if dist < min_distance:
                        min_distance = dist
                        closest_pair = (node, main_node)
            G.add_edge(*closest_pair)
            print(f"Connected {closest_pair[0]} to {closest_pair[1]} to unify components.")
    else:
        print("Graph is fully connected.")
    return G

def distance(u, v):
    return np.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

# Generate random positions within the given dimensions
def random_position(width, height):
    positions = {}
    i = 0
    while len(positions) < n:
        x = randint(0+1, width-1)
        y = randint(0+1, height-1)
        if (x, y) not in positions.values():
            positions[i] = (x, y)
            i += 1
    return positions
# Add nodes to the graph
def add_nodes(G, positions):
    for node, pos in positions.items():
        G.add_node(node, pos=pos)
    return G

## only add edges closest to each node based on fixed radius
def add_edges_by_fixed_radius(G, positions, fixed_radius):
    # Add edges based on distance
    for i in range(n):
        edges_per_node = 0
        for j in range(i + 1, n):
            dist = distance(positions[i], positions[j])
            print("dist: ", dist)
            # Probability of connection decreases within fixed radius
            if dist < fixed_radius:
                G.add_edge(i, j)
                print(f"Connected nodes {i} and {j} with distance {dist}")
                edges_per_node += 1
        print(f"Node {i} has {edges_per_node} edges.")
    return G


# Create an empty graph
G = nx.Graph()

# Number of nodes
n = 25  
# Area dimensions
width, height = n, n  
# fixed radius for nearest neighbors
fixed_radius = n/4

# Generate random positions for the nodes
positions = random_position(width, height)

# Add edges based on distance, edges are for nearest neighbors within fixed radius
G  = add_edges_by_fixed_radius(G, positions, fixed_radius)

# Check and connect isolated nodes
G = check_and_connect_isolates(G, positions)

# Check and connect components
G = connect_components(G, positions)

# Draw the graph
plt.figure()
nx.draw(G, pos=positions, node_size=200, with_labels=True, node_color='skyblue', edge_color='black',font_size=12, font_color='gray')

# Configure and show grid
plt.grid(True, which='both', color='gray', linewidth=0.8, linestyle='--')  # Ensuring the grid is visible
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Setting axis labels and ticks
plt.title('Simple Graph on a Grid')
plt.axis('on')  # Ensure the axis is shown
plt.xlabel('Width', fontsize=12)
plt.ylabel('Height', fontsize=12)
plt.xticks(range(0, width))  # Set ticks for x-axis
plt.yticks(range(0, height))  # Set ticks for y-axis
# Save the plot
plt.savefig(f"./random_graph_generator/nearest_neighbor/plots/nearest_neighbor_graph:{n}N_{fixed_radius}FR.png")
plt.show()
