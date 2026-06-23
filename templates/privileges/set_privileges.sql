-- this file sets the baseline privileges for the user bob
-- this is the user the student will alter the privileges of

grant connect on database testee to bob;
grant select on student to bob;