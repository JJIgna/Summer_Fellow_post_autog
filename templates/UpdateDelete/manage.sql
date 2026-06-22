------------------------------------------------------------------------------------------------- NO SQL ABOVE THIS LINE

--@--
insert into student
values ('12345', 'Jackson', 'Cybernetics', 97);
--@--
update student
set tot_cred = 95
where id = '11530';
--@--
delete from advisor
where s_id = '97101';
