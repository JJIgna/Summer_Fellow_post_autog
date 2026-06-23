--@_@--
-- as testee
select rolname from pg_roles where rolname = 'alice';
--@_@--
-- as alice
select name from student where id = '98423';
--@_@--
-- as bob
select * from student limit 1; -- this will fail
