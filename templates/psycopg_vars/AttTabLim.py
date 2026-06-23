"""
This is an example hw file using pysco pg
"""

import psycopg
from psycopg.rows import dict_row
from psycopg import sql
import os

def query(att, tab, lim):
    user = os.getenv("DB_USER")
    db = os.getenv("DB_NAME")
    with psycopg.connect("postgresql://"+user+"@localhost/"+db) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                sql.SQL("select {att} from {tab} limit (%s)").format(
                    att = sql.Identifier(att),
                    tab = sql.Identifier(tab)
                ),
                [lim]
            )
            return cur.fetchall()
