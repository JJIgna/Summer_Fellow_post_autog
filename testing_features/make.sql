CREATE DATABASE vehicle;

\c vehicle

CREATE TABLE car(
    num int,
    make varchar
);

INSERT INTO car values (2000, 'honda');