import networkx as nx

def create_graph(text):
    # Preprocess the text (tokenization, stop-word removal, stemming)
    preprocessed_text = preprocess_text(text)
    
    # Create a directed graph
    graph = nx.DiGraph()
    
    # Iterate through the preprocessed text
    for i in range(len(preprocessed_text) - 1):
        current_term = preprocessed_text[i]
        next_term = preprocessed_text[i + 1]
        
        # Add an edge between the current term and the next term
        graph.add_edge(current_term, next_term)
    
    return graph

def preprocess_text(text):
    # Implement your text preprocessing logic here
    # Tokenization, stop-word removal, stemming, etc.
    # Return the preprocessed text as a list of terms/words
    pass

# Example usage
document = "This is a sample document with some words."
graph = create_graph(document)