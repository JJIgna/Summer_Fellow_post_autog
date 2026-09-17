### Making a PTE

#### Step 1 - Make Your Assignment Write Up
Choose your questions and write the answers as a student would. (I assuming you are testing on the Univeristy DB)
Be sure to use the smart comments.

    --@_@--
    SELECT room_number
    FROM classroom
    WHERE capacity < 50;
    --@_@--
    SELECT name
    FROM student
    WHERE dept_name  'History';
    --@_@--
    SELECT s_id
    FROM advisor
    WHERE i_id = '59795';

Like this.

#### Step 2 - Make your Goldfile
The Goldfile goes under `docker_core/source`. Make its name disticnt compared to the name of the file the students will be submitting.
For all `select` statements, your Goldfile will match the assignmnet write up. For any `delete` or `insert` statements use a `select count(*)` to check the existance of the row. 

    -- answer 
    insert into table 
    values (a,b,c)
    -- goldfile
    select count(*) -- should be 1
    from table
    where (a,b,c)

    -- answer 
    delete from table 
    where (a,b,c)
    -- goldfile
    select count(*) -- should be 0
    from table
    where (a,b,c)

Create, privileges, and psycopg will be covered in another md

#### Step 3 - Make your `test_.py` file
Under `templates/Read` make a copy of `query_HW_template.py` in `docker_core/tests`. Do not put it in `test_kit`. Rename this file `test_[hw_name].py`. In this file will be a class with functions. These functions are your tests.

Following the order in your goldfile, for each select question make a copy of the function labled `select statememt` and for each insert or delete question make a copy of the function labled `insert/delete`.
Each test must named `test_...`. They run in alphabetical order so be sure to have leading zeros with numbers.

 - `@weight` denotes the number of point the question is worth
 - `@number` denotes the order the questions will have in gradescope
 - `@visibility` denotes how the question will show up. all options are found in `template_with_explanations`
 - `@timeout` denoted how long the test will run before failing
 
Edit these decorators to fit the needs of the assignment.

The name of the class will also appear in gradescope. This does not affect the testing or ordering in any way. It is something you may change if you so wish to. 

#### Step 4 - Dockerfile
To go `docker_core/Dockerfile`. In here are `ENV` statements you will need to modify. 

    ENV HW_NAME="name of file students will submit"
    ENV GOLD_FILE="name of your goldfile"
    ENV SOL_NUM="number of questions"

Do not touch any other `ENV` at this time.

#### Step 4 - Testing 
Take your assignment write up and put it in `docker_core/local_testing/submission`. Open bash and run these commands:

        cd docker_core
        docker compose build native
        docker compose run --rm -it native ../run_autograder 

Now check `docker_core/local_testing/results/results.json`. This will list all the test and thier results. All should say 'passed'. If any do not, check the error output and see if it is an error in your queries. If not, check `troubleshooting.md` for common errors. If none of those, ask me. 

#### Step 5 - Gradescope
In Bash, run:

    cd docker_core # if not there already
    docker build -t [username]/[classname]:[assingmentname] .
    docker push [username]/[classname]:[assingmentname]

This pushes the image into dockerhub. 

Now in gradescope, make a programming assignment. After setting up the name and due date, you will be brought to a screen with white circles on the left side. One of these will be labled Configure Autograder; click that one. Once there select the option for manual docker configuration. At the bottom, put in the name you gave the image in Bash. (This is the [username]/[classname]:[assingmentname]). Click Update Autograder and then click Test Autograder. This will then pull up a window where you can submit your assignment write up like a student would submit their homework. After submitting it will take a bit for the PTE to run, but one it does everything should come up green.

You are now done.

### Other notes

#### Other DBs
If you want to test on a different databases, there are few things you have to change. 

1. Pick the DB you want to test on. Available DBs can be found under `docker_core/archive` of the form `[name]_archive`. Currently only the University DB and SPP. 
2. Move the DB you want to test on into `docker_core/source`. Make sure to remove any other DB that may be in source. 
3. In `docker_core/DockerFile`, change the `BD_BUILD` env to the name of the DB you moved into source.
