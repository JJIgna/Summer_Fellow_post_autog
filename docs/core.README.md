# `docker_core`

---

## Introduction

Welcome to `docker_core`.  
This directory is the build context for the PTE docker image. It serves as storage for all the files that inhabit every image, 
and it is where the necessary files for a given testing instance are collected to produce its image. This README will go over the files
that permanently reside in this directory and exist in every PTE image. In short, they are: 

| File/Directory                      | usage                                    |
|-------------------------------------|------------------------------------------|
| [`Dockerfile`](#Dockerfile)         | builds image                             |
| [`compose`](#compose)               | assits in local testing                  |
| [`run_autograder`](#run_autograder) | start of autograder                      |
| [source](#source)                   | working directory inside container       |
| [tests](#tests)                     | contains all tests and helper class      |
| [misc](#misc)                       | not a specific file, they assist the PTE |

---

## `Dockerfile`

The base image is `gradescope/autograder-base:ubuntu-22.04`. `autograder-base` is used to allow easy integration with gradescope.
`ubuntu-22.04` is the lastest version that supports Postgres 18. This is important as it is the version used in class. 


The `Dockerfile` also contains a number of `ENV` commands. These are defined in the `Dockerfile` to for easy configuration.

HW_NAME
: Name of the homework file being tested. This tells the PTE the name of the file being tested so it can find it.

GOLD_FILE  
: Name of the gold file. A gold file is key for testing a piece of software. It set of good answers or a "correct" version
of the file being tested. This env is set so that the PTE can find the gold file.

SOL_NUM  
:  Number of expected solutions. This is so the PTE can inform the student of a discrepancy if it finds less than the given amount. 

DB_USER  
: This is the name of the default user that will be used to connect and queries a database every time.

DB_NAME 
: Like DB_USER, this is the name of the default database that will be queried.

DB_USER_SET
: Name of database user setup file. This filed is used to create the users that will be needed for testing.

DB_BUILD   
: Name of DB archive file. The PTE uses `pg_restore` to build the local DB from an archive acquired from `pg_dump`. If no
restoration is required for a test suite, then this env and be left as the empty string. 

PRIV_SET   
: Name of privilege set up file. As privileges can be set for a DB that doesn't exist yet, the default privileges have to 
set in a different file. This can be left as the empty string to forgo any privilege set up.

---

## `compose`

---

## `run_autograder`

---

## source

The source directory mimics the source directory found in the PTE container. It is the working directory and contains all 
the necessary files for the PTE to run. The files in source change depending on the suite, but these files always fall into 
source. 

| case               | files                     |
|--------------------|---------------------------|
| Every              | run_tests gold, dbUserSet |
| Quering premade DB | build file                |
| Testing Privileges | set_privileges            |


---

## tests

Though outside in the project, tests does end in source inside the PTE. Here is where the testing is suite placed.

---

## misc

---