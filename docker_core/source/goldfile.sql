--@_@-- From the department with the most instructors
with dept_num as(
    select department.dept_name, count(*) as c
      from department
               natural join instructor
      group by department.dept_name
    )
select dept_num.dept_name
from dept_num
where c = (
    select max(c)
    from dept_num
    );

--@_@-- Find the course that has been taken by the most students
with taken as(
    select course.title, count(*) as count
    from course natural join takes
    group by title
)
select title, count
from taken
where count = (
    select max(count)
    from taken
    );

--@_@-- Find the instructor that has taught the most total sections
with teaching as (
    select name, count(*) as c
    from instructor natural join teaches
    group by name
    order by c desc
    )
select name
from teaching
where c = (
    select max(c)
    from teaching
    );