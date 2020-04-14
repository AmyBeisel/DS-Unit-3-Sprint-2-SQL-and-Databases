# app/rpg_postgreSQL.py
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values  # so we can insert multiple rows at once
import json                 
import pandas as pd
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

conn = sq.connect(DB_FILEPATH)
print(type(conn)) #> <class 'psycopg2.extensions.connection'>

cur = conn.cursor()
print(type(cur)) #> <class 'psycopg2.extensions.cursor'>

conn.row_factory = sqlite3.Row

query_q1 = "SELECT * FROM armory_item;"
results1 = curs.execute(query_q1).fetchall()

#loads contents of the .env file into the scripts 
#added connection info to new db, postgre one

load_dotenv()
​
DB1_HOST = os.getenv("DB_HOST", default="OOPS")
DB1_NAME = os.getenv("DB_NAME", default="OOPS")
DB1_USER = os.getenv("DB_USER", default="OOPS")
DB1_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
​
connection = psycopg2.connect(dbname=DB1_NAME, user=DB1_USER, password=DB1_PASSWORD, host=DB1_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

# insertion_query and excute_values:
insertion_query = "INSERT INTO armory_item(item_id, name, value, weight) VALUES %s"
execute_values(cursor, insertion_query, results1)

#commit data
connection.commit()
cursor.close()
connection.close()

