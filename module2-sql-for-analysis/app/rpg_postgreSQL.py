# app/rpg_postgreSQL.py

import os
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values


load_dotenv() #> loads contents of the .env file into the script's environment

DB1_NAME = os.getenv("DB1_NAME")
DB1_USER = os.getenv("DB1_USER")
DB1_PASSWORD = os.getenv("DB1_PASSWORD")
DB1_HOST = os.getenv("DB1_HOST")


#Read the db file
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
print(type(connection)) #> <class 'sqlite3.Connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'sqlite3.Cursor'>

character = cursor.execute("SELECT * FROM charactercreator_character").fetchall()


#Connect to a PG database - in this case elephant SQL
connection = psycopg2.connect(dbname=DB1_NAME, user=DB1_USER, password=DB1_PASSWORD, host=DB1_HOST)
print(type(connection)) #>

cursor = connection.cursor()
print(type(cursor)) #>


#CREATE TABLE:
table_creation_query = """
-- DROP TABLE IF EXISTS charactercreator_character; 
CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level integer,
    exp integer,
    hp integer,
    strength integer,
    intelligence integer,
    dexterity integer,
    wisdom integer
);
"""
cursor.execute(table_creation_query)


#INSERT DATA INTO TABLE
insertion_query = """INSERT INTO charactercreator_character (
    character_id, 
    name, 
    level, 
    exp, 
    hp, 
    strength, 
    intelligence, 
    dexterity, 
    wisdom)
    VALUES %s
"""

#cursor.execute(insertion_query)
execute_values(cursor, insertion_query, character)



#commit data
connection.commit()
#close data
cursor.close()
connection.close()

