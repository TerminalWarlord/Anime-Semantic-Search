import os
from db import collection
from create_embeddings import create_embeddings



# Find documents where "embeddings" hasn't been set yet
r = collection.find({"embeddings": {"$exists": False}})


for i in r:
    title = i['name']
    
    # Join the alt names
    if 'other_names' in i:
        title+=' '.join(i['other_names'])
        
    # Add embeddings for the title to the DB
    collection.update_one({'_id':i['_id']}, {"$set":{ "embeddings": create_embeddings(title)}})
    print(i['_id'])