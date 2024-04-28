import os
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set up NLTK
nltk.download('punkt')

# Function to read documents from a folder
def read_documents(folder_path):
    documents = []
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
            documents.append(file.read())
    return documents

# Function to preprocess text (tokenization, removing stop words, etc.)
def preprocess_text(text):
    # You can perform any preprocessing steps here
    # For simplicity, let's just tokenize the text for now
    tokens = nltk.word_tokenize(text)
    return tokens

# Function to create a word co-occurrence graph
def create_word_cooccurrence_graph(documents):
    # Initialize CountVectorizer to count word occurrences
    vectorizer = CountVectorizer(tokenizer=preprocess_text)
    # Fit and transform the documents
    X = vectorizer.fit_transform(documents)
    # Compute the co-occurrence matrix
    co_occurrence_matrix = (X.T * X)
    # Create a graph
    G = nx.Graph()
    # Add nodes and edges based on co-occurrence
    for word, idx in vectorizer.vocabulary_.items():
        G.add_node(word)
    for i, j in zip(*co_occurrence_matrix.nonzero()):
        if i != j:
            word1 = vectorizer.get_feature_names_out()[i]
            word2 = vectorizer.get_feature_names_out()[j]
            weight = co_occurrence_matrix[i, j]
            if G.has_edge(word1, word2):
                G[word1][word2]['weight'] += weight
            else:
                G.add_edge(word1, word2, weight=weight)
    return G

# Function to create a document similarity graph
def create_document_similarity_graph(documents):
    # Initialize TfidfVectorizer to compute TF-IDF vectors
    vectorizer = TfidfVectorizer(tokenizer=preprocess_text)
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    # Compute cosine similarity between documents
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # Create a graph
    G = nx.Graph()
    # Add nodes and edges based on document similarity
    for i in range(len(documents)):
        G.add_node(f"Document {i+1}")
    for i in range(len(documents)):
        for j in range(i+1, len(documents)):
            similarity = similarity_matrix[i, j]
            G.add_edge(f"Document {i+1}", f"Document {j+1}", weight=similarity)
    return G

# Read documents from the folder
folder_path = "Health and Fitness"
documents = read_documents(folder_path)

# Create word co-occurrence graph
word_cooccurrence_graph = create_word_cooccurrence_graph(documents)

# Create document similarity graph
document_similarity_graph = create_document_similarity_graph(documents)

# Visualize word co-occurrence graph
plt.figure(figsize=(12, 8))
plt.title("Word Co-occurrence Graph")
pos = nx.spring_layout(word_cooccurrence_graph, k=0.3)
nx.draw(word_cooccurrence_graph, pos, with_labels=True, font_size=10, node_size=1500, node_color="skyblue", font_color="black")
plt.show()

# Visualize document similarity graph
plt.figure(figsize=(12, 8))
plt.title("Document Similarity Graph")
pos = nx.spring_layout(document_similarity_graph, k=0.3)
nx.draw(document_similarity_graph, pos, with_labels=True, font_size=10, node_size=1500, node_color="lightgreen", font_color="black")
plt.show()
