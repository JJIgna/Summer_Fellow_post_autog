"""
Query Execute:
    function for executing the queries Query Parse finds
parameters: path - path to .sql file
returns: this function is a generator. calling .__next__() will execute the next query
            the output of the execution is returned as a dictionary
"""

import psycopg
from psycopg.rows import dict_row
from testing_features.query_parse import query_parse
import os

def run_queries(path):

    url = os.getenv('DB_URL')

# establish connection
    with psycopg.connect(url) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
        # run query
           for q in query_parse(path):
               cur.execute(q)
               yield cur.fetchall()