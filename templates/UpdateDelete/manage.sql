------------------------------------------------------------------------------------------------- NO SQL ABOVE THIS LINE

--@_@--
insert into student
values ('12345', 'Jackson', 'Cybernetics', 97);
--@_@--
update student
set tot_cred = 95
where id = '11530';
--@_@--
delete from advisor
where s_id = '97101';
