from pymongo import MongoClient
import csv
import json


client = MongoClient('mongodb://m_admin:m_admin@localhost:27017')
with client:
    db = client.db
    count = db.res.count()
    k = db.res.find({'mesh_file': 'r0a0n20.xml'})
    print(list(k))
