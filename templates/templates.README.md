## Templates

This directory contains all the templates, examples, and set up files for all support testing methods. This document will 
provide How-Tos for each supported testing method.

| Table of Contents               |
|---------------------------------|
| [READ](#READ)                   |
| [UPDATE-DELETE](#UPDATE-DELETE) |
| [CREATE](#CREATE)               |
| [Privileges](#Privileges)       |
| [Psycopg](#Psycopg)             |

---

### READ

This is the most basic of testing methods. This method is used when only testing the READ part of CRUD. 
The gold file is a `.sql` and the student file is a `.sql` as well. Both contain answers to the assigned questions and 
both are expected to get rows. The rows from the gold file are used to check the rows from the student file. 

Here is the basic structure:

    # imports 
    # these are universal throughout the testing methods
    import unittest
    from gradescope_utils.autograder_utils.decorators import weight, number, visibility
    from timeout_decorator import timeout
    from test_kit.SQL_taker import SQLTaker
    import os

    class TestCaseName(unittest.TestCase):
        # set up QueryTaker instances for both the HW and gold files
        query = SQLTaker(os.getenv('HW_NAME'))      # gold file
        gold = SQLTaker(os.getenv('GOLD_FILE'))     # student file
    
    # TESTS ARE RAN IN ALPHABETICAL ORDER NOT ORDER THEY ARE DEFINED
    # THIS WILL AFFECT GRADING AS QUERIES FROM .sql FILES IS ORDER DEPENDENT
    
        @weight(1)
        @number("1")
        @visibility("visible")
        @timeout(5)
        def test_Query1(self): # ALL TESTS MUST START WITH test_
            # pull rows from both 
            true = self.gold.next_sql()
            out = self.query.next_sql()
            self.assertListEqual(out, true) # check against eachother

This structure continues through the rest of the testing methods.

---

### UPDATE-DELETE

These parts of CRUD are tested together as they perform similar actions to the database: data is changed in some way. This 
method also incorporates insert statements as they can all be tested the same way.

    # imports
    import unittest
    from gradescope_utils.autograder_utils.decorators import weight, number, visibility
    from timeout_decorator import timeout
    from test_kit.SQL_taker import SQLTaker
    import os

    class TestCaseName(unittest.TestCase):
        # set up QueryTaker instances for both the HW and gold files
        query = SQLTaker(os.getenv('HW_NAME'))      # gold file


The imports are the same as READ, and we still set up a `SQLTaker` for the gold and student files
    
    # -------------------------------------------------------------------------------
    # Syntax check, only the student file is executed                               
                                                                                    
        @number(1)                                                                  
        @weight(1)                                                                  
        def test_1insert(self):                                                     
            val = self.stu.next_sql(manage=True)                                    
            self.assertTrue(val, msg="error in insert statement")                   
                                                                                    
        @number(2)                                                                  
        @weight(1)                                                                  
        def test_2update(self):                                                     
            val = self.stu.next_sql(manage=True)                                    
            self.assertTrue(val, msg="error in update statement")                   
                                                                                    
        @number(3)                                                                  
        @weight(1)                                                                  
        def test_3delete(self):                                                     
            val = self.stu.next_sql(manage=True)                                    
            self.assertTrue(val, msg="error in delete statement")                   
                                                                                    
    # -------------------------------------------------------------------------------

Here is where we test the syntax. Each statement in the student file is executed and check for any errors. This is why we have 
`assertTrue` statements making checks. We will not get rows, but we may get an error.
    
    # -------------------------------------------------------------------------------
    # Content check, only gold file is run                                          
                                                                                    
        @number(4)                                                                  
        @weight(1)                                                                  
        def test_4values_insert(self):                                              
            true = self.gold.next_sql()                                             
            self.assertEqual(str(true), "[{'dept_name': 'Cybernetics'}]")           
                                                                                    
        @number(5)                                                                  
        @weight(1)                                                                  
        def test_5values_update(self):                                              
            true = self.gold.next_sql()                                             
            self.assertEqual(str(true), "[{'tot_cred': Decimal('95')}]")            
                                                                                    
        @number(6)                                                                  
        @weight(1)                                                                  
        def test_6values_delete(self):                                              
            true = self.gold.next_sql()                                             
            self.assertEqual(str(true), "[]")                                       
                                                                                    
                                                                                    
    # -------------------------------------------------------------------------------

Here is where we check the contents of the student file using the gold file. The idea is if the contents of the student file
are good, then they will have the desired effect on the database. So, the READ statements in the gold file check for the 
desired results from the student file. The key for these results is hard coded to avoid needing a gold database to test against.

---

### CREATE

This testing method uses a gold `.sql` file and a student `.sql` file. The student file contains SQL statements that create 
a database, create a table, and then populate that table. The gold file contains READ statements that check the contents of
the table. Other tests are performed within the structure of the test itself.

    import unittest
    from gradescope_utils.autograder_utils.decorators import weight, number, visibility
    from subprocess import run
    from test_kit.SQL_taker import SQLTaker
    import os
    import psycopg
    
    class PsqlF(unittest.TestCase):
    gold = SQLTaker(os.getenv('GOLD_FILE'))
    # only setup gold, student is run through -f

We have extra import for `run` from `subprocess`. This is used to run the student file The setup has changed as 
well as we only need a `SQLTaker` instance for the gold file. 

    @number(1)
    @weight(1)
    def test_bad(self):
        """
        syntax check
        """
        hw = os.getenv("HW_NAME")
        result = run("psql -U testee -h localhost -f" + hw, capture_output=True, shell=True)
        self.assertNotRegex(str(result.stderr), "ERROR", msg=f"syntax error in: {hw}")

Here we see the student file is run using `psql` with `-f.` This allows the student `.sql` file to contain postgres meta 
commands. To check for syntax errors the standard error from the command is check using regex for the word "error". 

    @number(2)
    @weight(1)
    def test_connection(self):
        """
        connection check
        """
        connect = False
        with psycopg.connect(os.getenv('DB_URL')):
            connect = True
        self.assertTrue(connect, msg="connection to database failed")

Here a connection test is made to the created database.

    @number(3)
    @weight(1)
    def test_values(self):
        """
        content check
        """
        true = self.gold.next_sql()
        self.assertEqual(str(true), "[{'make': 'honda'}]")

Finally, the gold file is executed to check the rows that were added to the created table. The expected rows are hardcoded 
to avoid needing a gold database for the test.

---

### Privileges

This method tests the creation of users/roles and the granting/revoking of privileges. It takes a student `.sql` file containing
SQL statements for user management and a gold `.sql` file for testing the users and their privileges.

    import unittest
    from gradescope_utils.autograder_utils.decorators import weight, number, visibility
    from test_kit.SQL_taker import SQLTaker
    import os

    class Priv(unittest.TestCase):
        gold = SQLTaker(os.getenv('GOLD_FILE'))
        stu = SQLTaker(os.getenv('HW_NAME'))

The imports and setup are simliar to read

    @number(1)
    @weight(1)
    def test_1_USER(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in create user statement")

    @number(2)
    @weight(1)
    def test_2_CONNECT(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in grant connect statement")

    @number(3)
    @weight(1)
    def test_3_SELECT(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in grant select statement")

    @number(4)
    @weight(1)
    def test_4_REVOKE(self):
        val = self.stu.next_sql(manage=True)
        self.assertTrue(val, msg="error in create revoke statement")

We execute the statements in the student file while checking for errors.

    @number(5)
    @weight(1)
    def test_5_role(self): # look for user in pg_role to check if created
        true = self.gold.next_sql()
        self.assertEqual(str(true), "[{'rolname': 'alice'}]", msg="user 'alice' not found")

    @number(6)
    @weight(1)
    def test_6_connectandselect(self): # test new user's privilege to select on a database
        true = self.gold.next_sql(user="alice")
        self.assertEqual(str(true), "[{'name': 'Alfaro'}]", msg="unable to access students")

    @number(7)
    @weight(1)
    def test_7values_delete(self):  # test is user bob had select privilege revoked
        true = self.gold.next_sql(user="bob")
        self.assertFalse(true, msg="user 'bob' can still access students")

Then we execute the gold file to test if the desired privilege changes were enacted.

---

### Psycopg

This test is different from the rest as it does not take a `.sql` from the student. Instead, it takes a Python file with 
function using the Psycopg package. The gold file is still a `.sql`. 

    import unittest
    from gradescope_utils.autograder_utils.decorators import weight, number
    from test_kit.SQL_taker import SQLTaker
    import os
    # we are testing a Python file, so we need to import the file to get the function
    import AttTabLim
    
    class TestRegion(unittest.TestCase):
        gold = SQLTaker(os.getenv("GOLD_FILE"))

We need to import the student made file to gain access to the Python function.

    @weight(1)
    def test_1(self):
        val = AttTabLim.query("name", "student", 1)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_2(self):
        val = AttTabLim.query("building", "department", 4)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_3(self):
        val = AttTabLim.query("grade", "takes", 7)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

    @weight(1)
    def test_4(self):
        val = AttTabLim.query("capacity", "classroom", 9)
        true = self.gold.next_sql()
        self.assertListEqual(val, true)

We call both the student function and gold file and compore the outputs. To understand this more, lets look at the student 
submission and the gold file.

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

Here is a sample student submission. The query the Psycopg code is executing has the form:

    select att
    from tab
    limit lim;

The gold file contains queries of this same form but with the parameters replaced with the arguments given in the test file.

    --@_@--
    select name
    from student
    limit 1;
    --@_@--
    select building
    from department
    limit 4;
    --@_@--
    select grade
    from takes
    limit 7;
    --@_@--
    select capacity
    from classroom
    limit 9;

The gold and student submission should produce the same rows if the student submission is correct. 