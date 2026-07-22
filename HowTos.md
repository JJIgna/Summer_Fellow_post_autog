## How To Use PTE

#### Step 0: What you need
For the autograder to work you need: 
* gold file
* `test_*.py`
* necessary setup

#### Step 1: Gold File
Make the gold for the test cases you plan to make. Depending on the test case, the gold file will be either a `.sql` or hardcoded rows.
Either way, these should be prepared ahead of time

#### Step 2: `test_*.py`
`test_*.py` is the file that contains the test suite. It consists of a class inheriting `unittest.Testcase` which allows
for the creation of test cases as functions. These test cases should be in the same order as in the gold file

#### Step 3: Necessary Setup 
Prepare any setup files that are needed to produce the appropriate testing environment. For quering a database, that would be an 
archive file. For testing privilege management that would be a `.sql` file that sets default privileges.

#### Step 4: `Dockerfile` Configuration
In the `Dockerfile` there are a number of `ENV` calls that set environment variables. Set these envs to the appropriate names for your
test suite.

#### Step 5: Put it all together
Assemble all the files into there respective directories in `docker_core`. `test_*.py` goes into the `tests` directory. 
All other files go into `source`.

#### Step 6: Build, Push, Configure
Build your PTE image. Push it to Docker Hub. Configure your assignment in gradescope to use your image.

---

## How To Make A Gold File

#### Step 1: Map out the assignment
You should have an idea of what you want to test. Your exact questions will be your outline for your gold file.

#### Step 2: Write the file 
This step can go two different ways: Query questions and Management questions.

READ test gold files are simple. Write the queries that give the correct answers to the questions in the assignment.
Put these in a `.sql` file with smart comments like a student would.

CREATE, UPDATE, and DELETE tests take a bit more planning. You need to write queries that test the structure of the database or 
the data. This means quering rows of newly added or deleted data. Attempting to connect to new databases. Connecting to the DB 
as different users to test their privileges. Whatever you are asking the students to do, you need to write queires that test wheter the
student's code had the correct effects. 

---

## How To Make A `test_*.py`

#### Step 1: Select Template
Select the template file that fit your current suite. It will be properly formated and ready for you to copy-paste the test cases.

#### Step 2: Fill out the test cases
This will change depending on what you are testing. READ tests will be arranged in the order of the questions. 
Management tests come in two parts. First, you need to test the syntax of the student's queries. Then, you need to test the 
contents using your gold file.

#### Step 3: Decorators
Add decorators to your tests to give them added information in Gradescope. These decorators include number, weight, and visibility. 
A timeout decorator can also be added to give a time limit to the queries. 

---