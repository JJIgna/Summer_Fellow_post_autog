--@--
create user alice with password 'private';
--@--
grant connect on testee to alice;
grant select on student to alice;
--@--
revoke select on student to bob;