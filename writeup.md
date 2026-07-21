# PostgreSQL Testing Environment

The PostgreSQL Testing Environment, or PTE, is an application designed to assist the instruction of database concepts by providing students with automated feedback. Specifically, this environment is designed to test PostgreSQL: a Rational Database Management System used in SLU's Database Systems and Security Course. The PTE is integrated with Gradescope's proprietary software.

This project was mentored by Dr. Ed Harcourt. As the professor of Database Systems and Security, he wanted a testing environment to help improve his student's learning. As one did not yet exist, Dr. Harcourt proposed this project to develop a testing environment that would meet the needs of the course.

This document is found within the project deliverable: the PTE directory. This directory contains all the code written to run the PTE as well as documentation and templates for all the supported testing schemes.

This directory also contains two PowerPoint presentations which I gave as progress updates to my fellow Fellows in the MCSS department. I gave a total of four presentations, but latter two were demos and did not use PowerPoint. 

The remainder of this document is split into two parts:

1. A description of the PTE's inner workings and its testing capabilities. 
2. Final thoughts on the Fellowship experience. 

## Inner Workings and Testing Capabilities.

The PTE is reliant on Gradescope's software as an API for all student and instructor interactions. Instructors can upload and manage tests while students can submit code to be tested and receive feedback. The testing environment itself takes the form of a Docker container running a testing script. 

A Docker container is an isolated program that ensures universality and repeatability. The container is made from a custom image with a base image from Gradescope. It initializes all necessary decencies for the testing script, including a PostgreSQL server running in the container. 

The testing script itself is written in Python using the Python Unittest module for test definition. A Gradescope library is used to automatically format the testing results to Gradescope's standard. All database connections for testing purposes are managed through Psycopg, and Python module designed for Postgres database interactions. 

The PTE supports a wide variety of tests including:

* The full suite of CRUD
    * CRUD stands for Create, Read, Update, and Delete. It describes the four major ways data can be manipulated and the four most commonly used when interacting with any database.
* Database creation and User Management
    * Database creation covers the other ways data can be manipulated through its organization. User management pertains to the management of user permissions to access and manipulate data.
* Psycopg script
    * Psycopg is a Python module that allows database connections and queries to be made to PostgreSQL servers.

These tests cover all instructional content, outside of theory, taught in CS345. It also covers the vast majority of ways students will be expected to interact with databases outside of the classroom.

## Final Thoughts on Fellowship

This summer was incredibly productive in multiple regards. 

Firstly, the project was completed on schedule. Ahead of schedule in fact. The final product exceeded expectations. Concepts thought to be untestable are now capable thought the PTE.

Secondly, the project required a large knowledge of not only programmatic knowledge but also organization and planning skills. This knowledge is not limited to this project and will be widely applicable to project outside of St. Lawrence. 

Lastly, this project acted as valuable experience working in the software development industry. It can be used as a baseline to guide future career decisions. 