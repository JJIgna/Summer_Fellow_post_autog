# escape=`

# Test Docker File
# Get Postgresql client installed on gradescope auotgrader base

#base image
FROM gradescope/autograder-base:ubuntu-22.04

# base directory
WORKDIR /autograder/source

# python
RUN apt-get install -y python3 python3-pip
RUN pip install "psycopg[binary]"
RUN pip install gradescope-utils

# potgresql
RUN apt install curl ca-certificates
RUN install -d /usr/share/postgresql-common/pgdg
RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
COPY pgdg.sources /etc/apt/sources.list.d/
RUN apt update
RUN apt install -y postgresql-client-18

# copy autograder files
COPY run_autograder /autograder/run_autograder
COPY run_test.py /autograder/source
COPY tests /autograder/source/tests
