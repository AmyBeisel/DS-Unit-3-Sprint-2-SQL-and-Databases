import sqlite3
import os

#DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print(type(conn)) #> <class 'sqlite3.Connection'>
curs = conn.cursor()
print(type(curs)) #> <class 'sqlite3.Cursor'>


query = """SELECT 
count(DISTINCT character_id) as character_count
FROM charactercreator_character"""

query1 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_cleric"""

query2 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_fighter"""

query3 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_mage"""

query4 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_thief"""



# results2 = curs.execute(query).fetchall()
# print("--------")
# print("RESULTS 2", results2)
print("----------")
result = curs.execute(query).fetchone()
print("RESULTS FOR CHARACTERCREATOR_CHARACTER", result)
print(result["character_count"])
print("-------------")
result1 = curs.execute(query1).fetchone()
print("Results for charactercreator_cleric", result1)
print(result1["character_ptr_count"])
print("---------")
result2 = curs.execute(query2).fetchone()
print("Results for charactercreator_fighter", result2)
print(result2["character_ptr_count"])
print("---------")
result3 = curs.execute(query3).fetchone()
print("Results for charactercreator_mage", result3)
print(result3["character_ptr_count"])
print('--------')
result4 = curs.execute(query4).fetchone()
print("Results for charactercreator_thief", result4)
print(result4["character_ptr_count"])



