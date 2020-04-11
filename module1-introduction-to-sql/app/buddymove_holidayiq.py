

import sqlite3 as sq
import os
import pandas as pd


df = pd.read_csv('./data/buddymove_holidayiq.csv')
df.rename(columns = {'User Id': 'User_Id'}, inplace = True)
conn = sq.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymove_holiday', conn)
