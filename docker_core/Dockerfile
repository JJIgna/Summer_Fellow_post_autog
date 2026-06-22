# escape=`

# PostgreSQL Testing Environment Dockerfile
#   This is the Dockerfile for creating a Testing Environment for PostgreSQL to run in Gradescope
#   It uses gradescope's autograder base image running ubuntu 22.04 and installs python3, psycopg, and
#       postgres-18

# base image
FROM gradescope/autograder-base:ubuntu-22.04

# base directory
# this sets the working directory
WORKDIR /autograder/source

# installing python
RUN apt-get install -y python3 python3-pip
RUN pip install "psycopg[binary]"
RUN pip install gradescope-utils
#   gradescope-utils is a package that add useful functions that help to
#   intergrate with the gradescope infrastucture
RUN pip install timeout-decorator

# installing potgresql
#   manual apt repository update required
RUN apt install curl ca-certificates
RUN install -d /usr/share/postgresql-common/pgdg
RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
COPY pgdg.sources /etc/apt/sources.list.d/
RUN apt update
RUN apt install -y postgresql-18
# set up .pgass file for the user created in dbsetup to assist with pg_restore
COPY --chmod=0600 .pgpass /root/

# environment variable set up.
# These varibles are call in places where they are needed
# This means they only need to be set here

ENV HW_NAME="manage.sql"
ENV GOLD_FILE="goldUD.sql"

# number of HW solutions or number of problems
ENV SOL_NUM="3"

# URL to the database that will be access for the HW
ENV DB_URL="postgresql://testee@localhost/testee"

# .sql file that sets up a defualt user
ENV DB_USER_SET="dbUserSet.sql"

# .sql file that contains statements for setting up user privileges
ENV PRIV_SET="priv.sql"

# this is the name of the file that is given to pg_restore
# set to "" to disable automatic DB building
ENV DB_BUILD="build"

# copy autograder files
COPY run_autograder /autograder/run_autograder
#   this is file is required by the gradescope infrastructure.
#   it is the start of the autograder and comtains some setup

COPY source /autograder/source
#   soucre contains all files and directories that need to be in
#   /autograder/source. These are:
#                           gold.sql
#                           dbUserSet.sql
#                           run_test.py
#                           build
#                           set_privileges.sql

COPY tests /autograder/source/tests
#   contains the files needed for testings. changes depending on the test
#   for Read:
#       test_kit
#       all test_*.py files containing the tests


