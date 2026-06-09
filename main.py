# test file
import psycopg
from psycopg.rows import dict_row
from region import Region

# python itself, if this doesn't work something has gone horribly wrong
print("Python Test")
print("Hello World")

# psycopg, please god work
print("Pyscopg Test")
print(psycopg.__version__)

# postgresql through psycopg
print("Postgresql Through Psycopg Test")
with psycopg.connect("postgres://jjigna23:jjigna23@hopper01.hpc.stlawu.edu:5432/spp_book") as conn:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            select distinct country
            from suppliers;
        """)

        print(cur.fetchall())

print(Region())

