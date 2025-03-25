from google import genai
from dotenv import load_dotenv
import os

load_dotenv()



client = genai.Client(api_key=os.environ("GEMINI_API_KEY"))

# result = client.models.embed_content(
#         model="gemini-embedding-exp-03-07",
#         contents="What is the meaning of life?")

# print(len(result.embeddings[0].values))