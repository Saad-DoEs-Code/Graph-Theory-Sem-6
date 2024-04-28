import sys

# Set default encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

import os
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

# Function to construct a directed graph for a document
def construct_graph(text):
    words = preprocess_text(text)
    G = nx.DiGraph()
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        if not G.has_edge(word1, word2):
            G.add_edge(word1, word2, weight=1)
        else:
            G[word1][word2]['weight'] += 1
    return G

# Function to compute document similarity based on common subgraphs
def compute_similarity(graph1, graph2):
    # Calculate Jaccard similarity of common subgraphs
    common_subgraphs = nx.graph_edit_distance(graph1, graph2)
    jaccard_similarity = 1 - (common_subgraphs / len(graph1) + len(graph2) - common_subgraphs)
    return jaccard_similarity

# Read text files from the folder
folder_path = "../Cleaning Text/Processed Data/Health and Fitness"
documents = defaultdict(str)

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file ends with ".txt"
    if file_name.endswith(".txt"):
        # Read the contents of the file and store it in the documents dictionary
        with open(os.path.join(folder_path, file_name), "r", encoding='utf-8') as file:
            documents[file_name] = file.read()

print(documents)
print(len(documents))
# Construct directed graphs for each document
document_graphs = {}
for doc_name, doc_text in documents.items():
    document_graphs[doc_name] = construct_graph(doc_text)
    print(document_graphs[doc_name])

# Compute document similarity
document_similarity = defaultdict(dict)
for doc1_name, graph1 in document_graphs.items():
    for doc2_name, graph2 in document_graphs.items():
        if doc1_name != doc2_name:
            similarity = compute_similarity(graph1, graph2)
            document_similarity[doc1_name][doc2_name] = similarity

# Visualize the constructed graphs (optional)
for doc_name, graph in document_graphs.items():
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=800, node_color='skyblue', edge_color='gray')
    plt.title(f"Graph for Document: {doc_name}")
    plt.show()

# Print document similarity
print("Document Similarity:")
for doc_name, similarities in document_similarity.items():
    print(f"{doc_name}:")
    for other_doc, similarity in similarities.items():
        print(f"\t{other_doc}: {similarity}")
