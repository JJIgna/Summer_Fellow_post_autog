import psycopg
from psycopg.rows import dict_row

def Region():
    with psycopg.connect("postgresql://jjigna23:g0ldh3art@hopper01.hpc.stlawu.edu:5432/spp_book") as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("""
                select distinct country
                from suppliers;
            """)
            return cur.fetchall()
