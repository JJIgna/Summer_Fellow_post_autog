# testing grounds for new features
import os
from test_kit.query_taker import QueryTaker

os.environ['DB_URL'] = "postgres://jjigna23@hopper01.hpc.stlawu.edu:5432/uni_full"

print("part")

q1 = QueryTaker("part.sql")
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())

print("gold")

q1 = QueryTaker("../docker_core/source/gold.sql")
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
print(q1.next_query())
