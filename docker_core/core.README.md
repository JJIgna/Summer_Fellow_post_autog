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


The `Dockerfile` also contains a number of `ENV` commands. 
The environment variables are used through the project and only need to be set in the `Dockerfile`. 

| variable    | definition                                      |
|-------------|-------------------------------------------------|
| HW_NAME     | name of homework file                           |
| GOLD_FILE   | name of gold file                               |
| SOL_NUM     | number of expected queries in a .sql file       |
| DB_USER     | name of database user that will used to connect |
| DB_NAME     | name of database to connect to                  |
| DB_USER_SET | name of the file which setups up default users  |
| PRIV_SET    |                                                 |
| DB_BUILD    |                                                 |

## `compose`

## `run_autograder`

## source

## tests

## misc
