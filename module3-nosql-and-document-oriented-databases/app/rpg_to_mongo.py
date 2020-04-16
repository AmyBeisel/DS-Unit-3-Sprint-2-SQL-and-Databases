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





