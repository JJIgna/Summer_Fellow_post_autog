# Letter to User

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
3. `testind_features`
   * this will most likely get removed at some point

Have fun. Happy Testing.

## _Jai-Jai Ignac_
