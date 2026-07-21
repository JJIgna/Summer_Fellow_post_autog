# PostgreSQL Testing Environment

Over the summer I developed the PostgreSQL Testing Environment, or PTE. PostgreSQL, also known as Postgres is a Relational Database Management System used in SLU's CS345 Database Systems and Security course. A testing environment is an instructional tool used to help programming students iterate on their code and acelerate their learning. 

This project was spured on by my mentor, Dr. Ed Harcourt's, want for a Postgres testing environment as one did not yet extist. Dr. Harocourt pitched the project to me because I wanted to do a fellowship related to Databases and had just taken CS345. I found it interging and thus we have the document you are reading now. This document, whether as a Markdown or Word file, came atteched to a directory containing this project's final devilerable: PTE version 1.0. This is the root version of the PTE that will be used in CS345 from the Fall of 2026 onward. This directory contains all the code that was written for the PTE as well as several documentation files and templates files for all supported testing schemas. 

The remainder of this document is split into two parts:

1. A description of the PTE's inner workings and its testing capabilities. 
2. Final thoughts on the Fellowship exprience. 

## Inner Workings and Testing Capabilities.

The PTE is reliant on Gradescope's software as an API for all student and instructor interactions. Intrusctors can uplaod and manage tests while students can submit code to be tested and recieve feedback. The testing environmet itself takes the form of a Docker container running a testing script. A Docker container is an isolated porgram that ensures universality and repeatablity. The container is made from a costum image with a base images from gradescope. It initializes all nessicary dependcies for the tesing script, including a Postgres server running in the container. The testing script itself is written in Python using the Python Unittest module for test definition. A Gradescope library is used to automatically format the testing results to Gradescope's standard. All database connections for testing purposes are managed through Psycopg, and Python module designed for Postgres database interactions. 

The PTE supports a wide varity of tests including:

* The full suite of CRUD
    * CRUD stands for Create, Read, Update, and Delete. It describes the four major ways data can be manipulated and the four most commonly used when interacting with any database.
* Database creation and User Managment
    * Database creation covers the other ways data can be manipulate through is organization. User management pertains to the management of user permissions to access and manipulate data.
* Psycopg script
    * As stated above, Psycopg is a Python module that allows for database connections and queries to be made to Postgres servers.

These tests cover all intructional content, outside of theory, taught in CS345. It also cover the vast majority of ways 

  