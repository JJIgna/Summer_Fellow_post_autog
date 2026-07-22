## `test_kit`

`test_kit` is a class and exception used to query `.sql` files. It is used in the `test_*.py` files. 

---

### `Query_Taker(path)`

`Query_taker` is the `.sql` parsing and executing class. A `Query_taker` instance take a `.sql` file with CRUD statements.
The statements are executed in order and only once. Psycopg is the package used to connect and access a given database.

#### Attributes:

`path`
: path to the `.sql` file

`done`
: a boolean used to mark when the end of the file has been reached 

`run`
: an instance of `smart_parse` on the `.sql` file

`num`
: integer value representing the number of statements found in the file

---

#### `smart_parse`
`smart_parse` is the parsing function. It uses a smart comment, `--@_@--`, to discern where a statement starts and ends.
A statement is defined as anything between either 2 smart comments or a smart comment and the end of the file. When the end of 
the `.sql` file is reached, `self.done` is marked as true.

Parameters:
* `self`
  * this function only takes `self` to access `self.path`

Returns:
* This function is a generator. On a call of `smart_parse.__next__()` the next statement in the `.sql` is returned as a string.

---

#### `execute_next`
`execute_next` is the executing function. It connects to a given database and runs the next statement found by `run`.

Parameters:
* `manage`
  * boolean marking if the statement to be executed is a management statement. these are not `SELECT` statements and do not give rows.
* `user`
  * set the user that will be used to access the database. if left blank, the default user will be used.
* `db`
  * set the database that will be connected to. if left blank, the default will be used.

Returns:
* when `manage` is `False`, `execute_next` will return all the rows of the executed query as a list. When `True`, it will return `True` on a successful execution.

---

#### `next_query`
`next_query` is the designated function for retrieving the outcome of the next query. It is designed to allow for safe calls 
of `smart_parse.__next__()` and grabs errors returned from `execute_next`. If `self.done` is `True`, all subsequent calls 
will raise `IncorrectQueryAmountError`

Parameters: These are the same parameters as `execute_next` and are simply passed on to `execute_next`.
* `manage`
  * boolean marking if the statement to be executed is a management statement. these are not `SELECT` statements and do not give rows.
* `user`
  * set the user that will be used to access the database. if left blank, the default user will be used.
* `db`
  * set the database that will be connected to. if left blank, the default will be used.

Returns: 
* returns the received output from `execute_next`. if it receives an exception, the exception is printed and `False` is returned.

---

### `wrong_number`

`wrong_number` contains the definition for the `IncorrectQueryAmountError`.

### `IncorrectQueryAmountError`
Expresses that an incorrect number of statements exist in an `.sql` file for a given test.

#### Attributes:

`expected`
: the expected number of statements

`found`
: the number of statements that would found.
