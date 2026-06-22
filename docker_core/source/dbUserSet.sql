/*
 * This is a sample dbUserSet.sql file.
 * This exists to set up the db users needed for the HW's context.
 * In this case, testee is just made to give the university db somewhere to go.
 * This is done to get around the fact that the default postgres user uses peer authentication in Linux
 *      and doesn't have a password.
 * We need a user with a password and a .pgpass file to preform certain other
 *      db set up actions like use an archive file with pg_restore to build the db.
 * It also gives us a user to connect to the db with through psycopg
 */
-- create user testee
CREATE USER testee WITH PASSWORD 'pass' SUPERUSER;
CREATE DATABASE testee;

CREATE USER bob WITH PASSWORD 'word';