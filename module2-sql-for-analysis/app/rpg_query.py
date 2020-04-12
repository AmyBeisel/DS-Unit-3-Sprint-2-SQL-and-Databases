
import sqlite3 as sq
import os
import pandas as pd

#DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

conn = sq.connect(DB_FILEPATH)
conn.row_factory = sq.Row

curs = conn.cursor()