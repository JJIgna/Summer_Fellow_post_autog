import psycopg
from psycopg.rows import dict_row
import os
from test_kit.wrong_number import IncorrectQueryAmountError


# Query Taker class
#   used when testing .sql files or when using .sql files

class QueryTaker:
    def __init__(self, path):
        self.path = path
        self.done = False
        self.run = self.smart_parse()
        self.num = 0

    # parser using smart comments (sm)
    def smart_parse(self):
        # buffer used to build query
        buff = []
        # check for if buff is collecting
        collecting = False

        # start of parser
        with open(self.path) as q:
            while c := q.read(1):

                # look for start sm
                if c == "@":
                    # take in next two characters
                    c = c + q.read(2)
                    # check for sm
                    if c == "@_@":
                        # if so, are we collecting?
                        if collecting:
                            # if found sm and collecting, we have encountered sm before
                            # must be at end of one query and star of a new one
                            # concat and yield current query before beginning the next one
                            yield ''.join(buff)
                            self.num += 1
                            buff.clear()
                            continue
                        # if not collecting, frist query of file
                        # so start collecting
                        collecting = True
                        continue

                # if collecting, then in a query section
                # add to buff
                if collecting:
                    buff.append(c)

        # hit end of file
        # final query ended before the end of the file
        # so build and yield
        self.done = True
        self.num += 1
        yield ''.join(buff)

    def execute_next(self, manage=False, user="", db=""):
        if user != "":
            username = user
        else:
            username = os.getenv("DB_USER")
        if db != "":
            dbname =  db
        else:
            dbname = os.getenv("DB_NAME")
        # establish connection
        with psycopg.connect("postgresql://" + username + "@localhost/" + dbname) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                # run query
                cur.execute(self.run.__next__())
                if not manage:
                    return cur.fetchall()
                else:
                    return True

    def next_query(self, manage=False, user="", db=""):
        if self.done:
            raise IncorrectQueryAmountError(os.getenv('SOL_NUM'), str(self.num))
        try:
            return self.execute_next(manage=manage, user=user, db=db)
        except Exception as e:
            print(f"error: {e}")
            return False
