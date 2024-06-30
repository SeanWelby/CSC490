import networkx as nx
import matplotlib.pyplot as plt
import gzip

# Initialize an empty graph
G = nx.Graph()

# Path to dataset file
file_path = r"C:\Users\swelb\OneDrive\Desktop\soc-LiveJournal1.txt.gz"

# Load the dataset
with gzip.open(file_path, 'rt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue  # Skip comments
        node1, node2 = map(int, line.split())
        G.add_edge(node1, node2)

print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

# Basic Analysis:

# Number of Nodes and Edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Degree Distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
plt.hist(degree_sequence, bins=100)
plt.title("Degree Histogram")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.yscale('log')
plt.xscale('log')
plt.show()
