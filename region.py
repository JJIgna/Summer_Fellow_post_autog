import psycopg
from psycopg.rows import dict_row

def region():
    with psycopg.connect("postgresql://testee:pass@localhost/testee") as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("""
                select name
                from instructor;
            """)
            return cur.fetchall()
