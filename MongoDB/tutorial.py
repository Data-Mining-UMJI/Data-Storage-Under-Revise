#! /usr/bin/python

from pymongo import MongoClient

client = MongoClient()

# Following two lines won't create an actual database/collection until the 1st insertion
db 			= client.test_database
collection 	= db.test_collection

import datetime

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
# print(post)
posts 	= db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

cur_collection = db.collection_names(include_system_collections=False)
print(cur_collection)

import pprint

pprint.pprint(posts.find_one())
