--@-- 1
SELECT DISTINCT s.ID, s.name -- see if any course the student has taken is in the set of Comp. Sci. courses
FROM student s, takes t
WHERE t.ID = s.ID
  AND t.course_id = some (   -- find the course_ids of all Comp. Sci. courses
    SELECT course_id
    FROM course
    WHERE dept_name = 'Comp. Sci.'
);

--@-- 2

);

--@-- 3
SELECT max(i.salary) max_salary, i.dept_name -- finds the max salary of instructors
                                             -- grouped by department
FROM instructor i, department d
WHERE i.dept_name = d.dept_name
GROUP BY i.dept_name;

--@-- 4
WITH max_salary(value) as ( -- relation of max salarys grouped by department
    SELECT max(i.salary)
    FROM instructor i, department d
    WHERE i.dept_name = d.dept_name
    GROUP BY i.dept_name
)
SELECT min(value) -- select minimum value from above relation
FROM max_salary;

