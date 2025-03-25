import os
from pymongo import MongoClient

# Connect to Mongodb
cluster = MongoClient(os.environ['MONGODB_URI'])
CDN = cluster["AnimeCDNBackUp"]
collection = CDN["AnimeCDNBackUp"]
