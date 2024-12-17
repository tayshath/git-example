import pandas as pd
import faiss
import numpy as np
from typing import List, Tuple
from dotenv import load_dotenv
from llm import LLMProxyOpenAIEmbeddings  # Assuming this is your LLM wrapper

# Load environment variables (for API keys, if needed)
load_dotenv()

# Initialize the embedding model
llm = LLMProxyOpenAIEmbeddings()

def search_faiss_with_combined_columns(
    df: pd.DataFrame, col1: str, col2: str, input_values: Tuple[str, str], faiss_index_path: str, top_k: int = 5
) -> List[Tuple[int, float]]:
    """
    Search a FAISS index using combined cell values as input.

    Args:
        df (pd.DataFrame): DataFrame containing original text data.
        col1 (str): Name of the first column.
        col2 (str): Name of the second column.
        input_values (Tuple[str, str]): Tuple of two strings representing the cell values from the two columns.
        faiss_index_path (str): Path to the FAISS index file.
        top_k (int): Number of top matches to retrieve. Defaults to 5.

    Returns:
        List[Tuple[int, float]]: List of tuples containing indices and similarity scores of top matches.
    """
    # Combine input cell values
    combined_input_text = input_values[0] + " " + input_values[1]
    
    # Load the FAISS index
    index = faiss.read_index(faiss_index_path)

    # Generate embedding for the combined input text
    query_embedding: np.ndarray = llm.embed_text(combined_input_text)
    query_embedding = np.array([query_embedding]).astype("float32")

    # Normalize the query embedding for cosine similarity
    faiss.normalize_L2(query_embedding)

    # Search for the top K similar embeddings
    distances, indices = index.search(query_embedding, top_k)

    # Return the top matches with their similarity scores
    return list(zip(indices[0], distances[0]))

# Example usage
df = pd.read_excel("input.xlsx")  # Load your original Excel file

# Specify cell values from two columns to search
input_values = ("Sample value from Column1", "Sample value from Column2")

results = search_faiss_with_combined_columns(df, "Column1", "Column2", input_values, "faiss_index.index", top_k=5)

print("Top matches:")
for idx, score in results:
    print(f"Index: {idx}, Similarity Score: {score}")
    print(f"Matched Text: {df.loc[idx, 'Column1']} {df.loc[idx, 'Column2']}")
