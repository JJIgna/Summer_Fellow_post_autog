# escape=`

# PostgreSQL Testing Environment Dockerfile
#   This is the Dockerfile for creating a Testing Environment for PostgreSQL to run in Gradescope
#   This file does not need to be alter to fit different testing suites. Only the contents of soure,
#       run_autograder, and tests need to be changed to fit current needs
#   It uses gradescope's autograder base image running ubuntu 22.04 and installs python3, psycopg, and
#       postgres-18

# base image
FROM gradescope/autograder-base:ubuntu-22.04


# base directory
WORKDIR /autograder/source

# installing python
RUN apt-get install -y python3 python3-pip
RUN pip install "psycopg[binary]"
RUN pip install gradescope-utils
#   gradescope-utils is a package that add useful functions that help to
#   intergrate with the gradescope infrastucture

# installing potgresql
#   manual apt repository update required
RUN apt install curl ca-certificates
RUN install -d /usr/share/postgresql-common/pgdg
RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
COPY pgdg.sources /etc/apt/sources.list.d/
RUN apt update
RUN apt install -y postgresql-18
COPY --chmod=0600 .pgpass /root/

ENV HW_NAME="part.sql"
ENV GOLD_FILE="gold.sql"
ENV DB_URL="postgresql://testee:pass@localhost/testee"
ENV DB_SETUP="dbsetup.sql"
ENV DB_BUILD="build"

# copy autograder files
COPY run_autograder /autograder/run_autograder
#   this is file is required by the gradescope infrastructure.
#   it contains a bash script that starts the tests

COPY source /autograder/source
#   soucre contains all files and directories that need to be in
#   /autograder/source. commonly the python script that runs the tests

COPY tests /autograder/source/tests
#   tests contains everything needed for the tests


