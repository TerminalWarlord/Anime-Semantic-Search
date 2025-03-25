from create_embeddings import create_embeddings
from db import collection



# Search in MongoDB
def search():
  q = input("Enter a query to search:")
  
  # Generate query embedding
  vector = create_embeddings(q)

  results = collection.aggregate([
    {
      "$vectorSearch": {
        "index": "titleSemanticSearch",
        "path": "embeddings",
        "queryVector": vector,
        "numCandidates":10000,
        "limit": 20
      }
    }
  ])  


  for i in results:
      print(i['name'])

if __name__=='__main__':
  search()