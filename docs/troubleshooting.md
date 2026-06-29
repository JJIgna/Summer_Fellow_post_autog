## Trouble Shooting and Common Errors

### False negative
* The simplest thing that can cause a false negative is sql in the wrong order. Make sure sql statements are in the same order 
in the gold and student files. 
* Another cause can be errors in the formating of hardcoded keys. Because these keys and answers are checked as strings ever 
character has to be the same. Try finding the `psycopg` output for the READ query to are testing and copy|paste the output as 
your key to ensure the same formating

### Incorrect Statement Amount Error
If this is raising when it shouldn't be, check the smart comments. If these are not formated or placed correctly then the 
statements will not be parsed correctly leading to skipped to improperly ran statements.

### Passwords
Make sure every user that will be needed for setup and tests has their password for the required database in the `.pgpass`
file. If the password is not in the .pgpass file then psycopg will be able to connect to the database and the setup commands
will be stuck waiting for a password input. This can cause false positives and a failure of the whole PTE.  

### Test Case Names
Make sure each test case has a distinctive name. If two test cases have the same name, `unittest` will treat them as one test. 
