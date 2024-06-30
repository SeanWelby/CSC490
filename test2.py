import networkx as nx
import matplotlib.pyplot as plt
import gzip
from itertools import islice

# Initialize an empty graph
G = nx.Graph()

# Path to dataset file
file_path = r"C:\Users\swelb\OneDrive\Desktop\soc-LiveJournalJune11.txt.gz"

# Load a subset of the dataset for quicker analysis
def load_graph_subset(file_path, num_lines=1000000):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in islice(f, num_lines):
            if line.startswith('#'):
                continue  # Skip comments
            node1, node2 = map(int, line.split())
            G.add_edge(node1, node2)

load_graph_subset(file_path, num_lines=100000)  # Adjust num_lines as needed

# Find the largest connected component
largest_component = max(nx.connected_components(G), key=len)

# Visualize the largest connected component
largest_comp_graph = G.subgraph(largest_component).copy()

plt.figure(figsize=(12, 12))
pos = nx.spring_layout(largest_comp_graph)
nx.draw(largest_comp_graph, pos, node_size=10, node_color="red", edge_color="gray", alpha=0.5)
plt.title("Visualization of the Largest Connected Component")
plt.show()
