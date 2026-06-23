"""
This is an example hw file using pysco pg
"""

import psycopg
from psycopg.rows import dict_row
import os

def region():
    user = os.getenv("DB_USER")
    db = os.getenv("DB_NAME")
    with psycopg.connect("postgresql://"+user+"@localhost/"+db) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("""
                select name 
                from student 
                where id = '77898';
                        """)
            return cur.fetchall()
