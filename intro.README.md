# Letter to User
# PTE Version 1.0

---

Hello,  
This is the project directory for the PostgreSQL Testing Environment (PTE). This directory contains all the needed files 
and information to run the PTE through Gradescope using Docker. The PTE was created by me as a St. Lawrence University Fellows Summer
Research Project (SLUFSRP). It was created to be used in CS345 Database Systems and Security to assist in teaching and 
learning PostgreSQl.

The PTE (currently) makes use of Gradescope's Autograder infrastructure to run. It uses a modified Autograder base image setup 
to run a local PostgreSQL database to test all parts of the DDL and DML. DB connection is done through Psycopg, a Python package
designed to work with PostgreSQL.

This directory contains three subdirectories:

1. `docker_core`
   * This is the build context for the PTE image. 
2. `templates`
   * This contains all the example abd template files for the different kinds of tests that can be conducted.
3. `Tutorial`
   * This is a basic tutorial walking through how to make a PTE for testing READ statements

There are also two other `Markdown` files : 
1. `HowTos`
   * A few basic How-Tos for setting up the PTE
2. `troubleshooting` 
   * a few troubleshooting notes

Have fun. Happy Testing.

## _Jai-Jai Ignac_
