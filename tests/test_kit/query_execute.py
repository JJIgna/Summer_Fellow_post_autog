"""
Testing framework for queries from an .sql file
"""

import psycopg
from psycopg.rows import dict_row
from test_kit.query_parse import query_parse

def run_queries(path):

# establish connection
    with psycopg.connect("postgresql://testee:pass@localhost/testee") as conn:
        with conn.cursor(row_factory=dict_row) as cur:
        # run query
           for q in query_parse(path):
               cur.execute(q)
               yield cur.fetchall()