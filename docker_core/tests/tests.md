# Tests

This document breaks down every part of a `test_*.py` file. It will give explanations and describe how to use each part.

| Table of Contents                         |
|-------------------------------------------|
| [Anatomy](#Anatomy)                       |
| [Unittest and Names](#Unittest_and_Names) |
| [Setup](#Setup)                           |
| [Decorators](#Decorators)                 |
| [Value Collection](#Value_Collection)     |
| [Assert](#Assert)                         |

---

## Anatomy

There are three main parts to a `test_*.py` file: the class definition, the setup, and the test cases . The test cases 
also have three parts: the decorators, value collection, and `assert` statements. There are also imports, but these stay
the same in every file, so they will not be covered here.

    # class defintion
    class TestCaseName(unittest.TestCase):
    
        # setup
        query = SQLTaker(os.getenv('HW_NAME'))
        gold = SQLTaker(os.getenv('GOLD_FILE'))
        
        # tests themselves
        # decorators 
        @weight(1)
        @number("1")
        @visibility("visible")
        @timeout(5)
        def test_Query1(self):
            # collection of values
            true = self.gold.next_sql()
            out = self.query.next_sql()
            # assert
            self.assertListEqual(out, true)

This example is for READ tests.

---

## Unittest_and_Names

Before we move on to each selection, I want to quickly note why these files have this structure and how to name them, as 
they are related. 

These files are built using `unittest`, an object-oriented Python testing package. It defines a class `TestCase` makes a set 
of test cases. The individual tests are defined as functions. This comes with some important conventions.
1. The files must have `test_` in the beginning. This is how `unittest` knows the file has a `TestCase`.
2. Though the class doesn't have any naming conventions, it must inherit the `TestCase` class.
3. Each test case in the class must have `test_` in the beginning of its name, much like the file.
4. Tests run in alphabetical order using their names. This is very important as the nature of the PTE makes the tests order
sensitive. So, __make sure the name of the tests reflect their order so they run correctly.__ This is not as important for READ tests
because as long as the student file and gold file are always executed at the same time, it will check correctly just under the wrong test name.
_However_, this is major concern for management test that have hardcode keys. So, __make sure the name of the tests reflect their order so they run correctly.__

---

## Setup

The main things that will be setup are `SQLTaker` instances for the gold and or student files. We want these as class varibles 
so they can be accessed bt each test. `unittest` does have `setUp` and `tearDown` as builtins, but they run for every test
are therefore not useful for testing up our `SQLTaker` instances.

This is also where an instance variable for a Psycopg function will be defined.

---

## Decorators

The PTE makes use of four decorators. Three are from Gradescope's `autograder_utils` and one is from a package called 
`timeout_decorator`.

`@weght`
: This defines the number of points a test is worth

`@number`
: This gives each test a number or value associated with it. This value is what Gradescope uses to order the tests.

`@visibility`
: This determines how and when the student sees the test case. Here all the values `@visibility` can be set to:

* `hidden`: test case will never be shown to students
* `after_due_date`: test case will be shown after the assignment's due date has passed.
  If late submission is allowed, then test will be shown only after the late due date.
* `after_published`: test case will be shown only when the assignment is explicitly
        published from the "Review Grades" page
* `visible` (default): test case will always be shown

These all come form the official Gradescope documentation.

`@timeout`
: Sets a timeout timer for the given number of seconds. If runs longer than the timer, the test case is failed.

---

## Value_Collection

This is where the output from a `SQLTaker` or Psycopg function is collected. When collected from both a student and a gold 
file, call the gold file frist. This way if any error occurs when calling the student file and the whole test raises, the gold file 
will still iterate and the following tests will proceed normally.

---

## Assert

Here is where the answer check is made using the `unittest` `self.assert`. There are many `aseert` statements. There are four 
used for the PTE:

`assertEqual`
: This checks using ==. This used when checking against a hardcode key. The output from `SQLTaker` will need to be converted
to a string.

`assertListEqual`
: This is used when checking two lists when you have a gold and student `.sql`.

`assertTrue` and `assertFale`
: These check if a value is true or false, respectively. These are used when checking CREATE, UPDATE, and DELETE statements. `assertTrue` is used
when checking syntax. `assertFalse` is used when checking a removed or absent privilege. 


