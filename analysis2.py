import networkx as nx
import matplotlib.pyplot as plt
import gzip

file_path_june11 = r"C:\Users\swelb\OneDrive\Desktop\soc-LiveJournalJune11.txt.gz"
file_path_june16 = r"C:\Users\swelb\OneDrive\Desktop\soc-LiveJournal16.txt.gz"

def load_graph(file_path):
    G = nx.Graph()
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue  # Skip comments
            node1, node2 = map(int, line.split())
            G.add_edge(node1, node2)
    return G

G_june11 = load_graph(file_path_june11)
G_june16 = load_graph(file_path_june16)

def calculate_influence(graph, weight1=1, weight2=1):
    influence = {}
    for node in graph.nodes():
        degree = graph.degree(node)
        neighbors = graph.neighbors(node)
        neighbor_degree_sum = sum(graph.degree(n) for n in neighbors)
        influence[node] = degree * weight1 + neighbor_degree_sum * weight2
    return influence

influence_june11 = calculate_influence(G_june11)

influence_june16 = calculate_influence(G_june16)

most_influential_june11 = max(influence_june11, key=influence_june11.get)
print(f"Most influential node on June 11: Node {most_influential_june11} with influence {influence_june11[most_influential_june11]}")

most_influential_june16 = max(influence_june16, key=influence_june16.get)
print(f"Most influential node on June 16: Node {most_influential_june16} with influence {influence_june16[most_influential_june16]}")
