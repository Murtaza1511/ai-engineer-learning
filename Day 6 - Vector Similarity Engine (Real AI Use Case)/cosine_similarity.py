import numpy as np

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1) # Calculate the L2 norm (magnitude) of vec1
    norm_vec2 = np.linalg.norm(vec2) # Calculate the L2 norm (magnitude) of vec2
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0  # Avoid division by zero
    
    return dot_product / (norm_vec1 * norm_vec2)

def analyze_similarity(vec1, vec2):
    """Analyze the similarity between two vectors and provide insights."""
    similarity = cosine_similarity(vec1, vec2)
    
    if similarity > 0.8:
        return f"The vectors are very similar with a cosine similarity of {similarity:.2f}."
    elif similarity > 0.5:
        return f"The vectors are moderately similar with a cosine similarity of {similarity:.2f}."
    else:
        return f"The vectors are not similar with a cosine similarity of {similarity:.2f}."
    
# Example usage
if __name__ == "__main__":
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([2, 4, 6])
    vector3 = np.array([4, 5, 6])
    vector4 = np.array([0, 0, 0])
    vector5 = np.array([1, 0, 0])  

    
    print(analyze_similarity(vector1, vector2))  
    print(analyze_similarity(vector1, vector3))  
    print(analyze_similarity(vector1, vector4))
    print(analyze_similarity(vector1, vector5))