--@_@-- From the department with the most instructors
    select department.dept_name, count(*) as c
      from department
               natural join instructor
      group by department.dept_name