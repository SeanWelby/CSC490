import networkx as nx
import gzip  # Ensure gzip is imported
from karateclub import DeepWalk
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module='numpy')

# Function to load a subset of the graph
def load_graph(file_path, max_nodes=None):
    G = nx.Graph()
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        count = 0
        for line in f:
            if line.startswith('#'):
                continue  # Skip comments
            if max_nodes is not None and count >= max_nodes:
                break  # Stop loading after max_nodes
            node1, node2 = map(int, line.split())
            G.add_edge(node1, node2)
            count += 1
    return G

# Function to reindex the graph nodes from 0 to n-1
def reindex_graph(G):
    mapping = {node: i for i, node in enumerate(G.nodes())}
    return nx.relabel_nodes(G, mapping)

# Path to dataset file
file_path = r"C:\Users\swelb\OneDrive\Desktop\soc-LiveJournalJune11.txt.gz"
# Adjust max_nodes as needed to fit within memory constraints
max_nodes = 100000  # Set a limit to avoid memory issues

# Load the dataset (subset if max_nodes is set)
G = load_graph(file_path, max_nodes=max_nodes)

# Reindex the graph nodes
G = reindex_graph(G)

# Adjust parameters for DeepWalk to optimize memory usage
model = DeepWalk(walk_number=10, walk_length=20)

# Fit DeepWalk model to the graph
model.fit(G)
embeddings = model.get_embedding()

# Convert embeddings to a dictionary
embedding_dict = {str(i): emb for i, emb in enumerate(embeddings)}

# Rank nodes using PageRank
pagerank = nx.pagerank(G)

# Sort nodes by PageRank scores
sorted_pagerank = sorted(pagerank.items(), key=lambda item: item[1], reverse=True)

# Print the top 10 most influential nodes based on PageRank
print("Top 10 most influential nodes based on PageRank:")
for i in range(10):
    print(f"Node {sorted_pagerank[i][0]}: PageRank {sorted_pagerank[i][1]}")

# Visualize the embeddings using t-SNE for dimensionality reduction
tsne = TSNE(n_components=2)
node_positions = tsne.fit_transform(embeddings)

plt.figure(figsize=(10, 10))
plt.scatter(node_positions[:, 0], node_positions[:, 1], s=1)
plt.title("Node Embeddings Visualization")
plt.show()
