--@_@--
create user alice with password 'private';
--@_@--
grant connect on database testee to alice;
--@_@--
grant select on student to alice;
--@_@--
revoke select on student from bob;