from google import genai
from dotenv import load_dotenv
import os
import numpy as np 
from sentence_transformers import SentenceTransformer



load_dotenv()


def create_embeddings(text: str)->list[float]:
    # Gemini allows 15 req/min on the free plan
    # 1500 req/day
    # generates embeddings with 3072 dimensions
    
    # client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    # result = client.models.embed_content(
    #         model="gemini-embedding-exp-03-07",
    #         contents=text)
    # return result.embeddings[0].values
    
    
    
    # sentence-transformers (all-MiniLM-L6-v2) is opensourced, no limitation other than 
    # it generates embeddings with 384 dimensions
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(text)
    
    # Convert the numpy array to list
    return np.array(embeddings).tolist()

    
    