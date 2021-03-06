# app/insert_titanic.py

import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


load_dotenv() #> loads contents of the .env file into the script's environment

DB2_NAME = os.getenv("DB2_NAME")
DB2_USER = os.getenv("DB2_USER")
DB2_PASSWORD = os.getenv("DB2_PASSWORD")
DB2_HOST = os.getenv("DB2_HOST")

#Read CSV
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)
df.index += 1
print(df.head())

#Connect to pg database - in this case elephant sql
connection = psycopg2.connect(dbname=DB2_NAME, user=DB2_USER, password=DB2_PASSWORD, host=DB2_HOST)
print(type(connection)) #>

cursor = connection.cursor()
print(type(cursor)) #>


# CREATE TABLE

table_creation_query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""

cursor.execute(table_creation_query)

query = "SELECT count(DISTINCT id) FROM passengers"
cursor.execute(query)
result = cursor.fetchone() 
if result[0] == 0:
    



    #INSERT DATA INTO TABLE
    list_of_tuples = list(df.to_records(index = True))

    insertion_query = f"INSERT INTO passengers (id, survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
    execute_values(cursor, insertion_query, list_of_tuples)


#commit
connection.commit()
#close 
cursor.close()
connection.close()