# escape=`

# PostgreSQL Testing Environment Dockerfile
#   This is the Dockerfile for creating a Testing Environment for PostgreSQL to run in Gradescope
#   This file does need to be alter to fit different testing suites. Only the contents of soure,
#       run_autograder, and tests need to be changed to fit current needs
#   It uses gradescope's autograder base image running ubuntu 22.04 and installs python3, psycopg, and
#       postgres-18

#base image
FROM gradescope/autograder-base:ubuntu-22.04

# base directory
WORKDIR /autograder/source

# installing python
RUN apt-get install -y python3 python3-pip
RUN pip install "psycopg[binary]"
RUN pip install gradescope-utils

# installing potgresql
#   manual apt repository update required
RUN apt install curl ca-certificates
RUN install -d /usr/share/postgresql-common/pgdg
RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
COPY pgdg.sources /etc/apt/sources.list.d/
RUN apt update
RUN apt install -y postgresql-18

# copy autograder files
COPY run_autograder /autograder/run_autograder
COPY source /autograder/source
COPY tests /autograder/source/tests


