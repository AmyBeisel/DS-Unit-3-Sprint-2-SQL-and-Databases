"""
The difference between MongoDB and PostgreSQL
is in the way you read and write the data.
For example, when importing in PostgreSQL you look 
at the entire row, while for Mongo you have to assign a value
to each column.
The advantage of Mongo is that you don't need a schema.
However, having a well defined relational schema in postgres
helps us retreiving more information and relationships between tables.
I would say it's easier to work with postgres when having structured data,
and to work with mongo when having unstructured data.

"""

import pymongo
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv() #loads env vars from the .env file

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

#db = client.rpg


# Connect to sqlite rpg database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
print(type(conn))
cursor = conn.cursor()
print(type(cursor))

character = cursor.execute("SELECT * FROM charactercreator_character").fetchall()
#print("DB:", type(db), db)

db = client.character # "rpg_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.rpg_mongo # "rpg_mongo" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)




# #Getting a colletion (tables in RDBMS)
# character = cursor.execute("SELECT * FROM charactercreator_character").fetchall()
# collection = db.rpg
# print(db.list_collection_names())

# # Get table names from the rpg database

# table_creation_query = {

#     "character_id", 
#     "name",
#     "level integer",
#     "exp",
#     "hp",
#     "strength" ,
#     "intelligence",
#     "dexterity",
#     "wisdom" 
# }

# cursor.execute(table_creation_query)


# #INSERT DATA INTO TABLE
# insertion_query = {
#     "character_id", 
#     "name", 
#     "level", 
#     "exp", 
#     "hp", 
#     "strength", 
#     "intelligence", 
#     "dexterity", 
#     "wisdom"
    
# }

# #cursor.execute(insertion_query)
# execute_values(cursor, insertion_query, character)




# team = [table_creation_query, insertion_query, character]
# collection.insert_many(team)
# print("DOCS:", collection.count_documents({}))

# high_levels = list(collection.find({"level": {"$gte": 70}}))
# for doc in high_levels:
#     print(doc["name"])














