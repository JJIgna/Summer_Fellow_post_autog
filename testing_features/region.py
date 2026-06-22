import psycopg
from psycopg.rows import dict_row

def region():
    with psycopg.connect("postgresql://jjigna23@hopper01.hpc.stlawu.edu/uni_full") as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("""
                select *
                from student 
                where id = '12345';
                        """)
            return cur.fetchall()
