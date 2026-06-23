/*
 * This is the example HW file for query HW using .sql files.
 * Yes I am aware it is the same as the example HW file, but that is on purpose.
 * The two files will end up looking similar as they need to be formatted similarly.
 * That being they will need to follow the smart comment rules for execution.
 * This is the smart comment --@_@--
 * Queries are defined as anything between two of those comments or the end of the file.
 * Other text is allowed to follow that comment.
 * The order of the Read will need to be the same between the gold and HW file.
 * BE SURE TO FOLLOW THIS RULE. OTHERWISE, THE HW WILL NOT BE TESTED CORRECTLY
 * Dummy Read, blank Read, or even syntax errors are allowed in the designated query spaces.
 * You can skip other Read and submit fewer Read than expected and not affect other tests.
 * Submitting fewer than expected Read will raise an exception displaying the number of Read submitted and
 *  the number expected.
 */


------------------------------------------------------------------------------------------------- NO SQL ABOVE THIS LINE

--@_@-- 1
SELECT DISTINCT s.ID, s.name -- see if any course the student has taken is in the set of Comp. Sci. courses
FROM student s, takes t
WHERE t.ID = s.ID
  AND t.course_id = some (   -- find the course_ids of all Comp. Sci. courses
    SELECT course_id
    FROM course
    WHERE dept_name = 'Comp. Sci.'
);

--@_@-- 2
SELECT s.ID, s.name
FROM student s
WHERE NOT EXISTS( -- try to make a relation of classes that student has taken before 2005
                  -- if the relation does not exists, then the student has not taken anny class before 2005
    SELECT *
    FROM takes t
    WHERE s.ID = t.ID and t.year < 2005
);

--@_@-- 3
SELECT max(i.salary) max_salary, i.dept_name -- finds the max salary of instructors
                                             -- grouped by department
FROM instructor i, department d
WHERE i.dept_name = d.dept_name
GROUP BY i.dept_name;

--@_@-- 4
WITH max_salary(value) as ( -- relation of max salarys grouped by department
    SELECT max(i.salary)
    FROM instructor i, department d
    WHERE i.dept_name = d.dept_name
    GROUP BY i.dept_name
)
SELECT min(value) -- select minimum value from above relation
FROM max_salary;

--@_@-- 5
WITH Acc_Stu(ID, name, adv_ID) as ( -- relation of Accounting id and name with id of their advisors
    SELECT s.ID, s.name, a.i_ID
    FROM student s, advisor a
    WHERE s.dept_name = 'Accounting' and s.ID = a.s_id
)
SELECT a.ID, a.name -- finds accounting students you adisvors are in physics department
FROM Acc_Stu a, instructor i
WHERE i.ID = a.adv_ID and i.dept_name = 'Physics';

--@_@-- 6
SELECT dept_name
FROM department
WHERE budget > (
    SELECT budget -- gets budget of the Language department
    FROM department
    WHERE dept_name = 'Languages'
)
ORDER BY dept_name;

--@_@-- 7
WITH retake(course, stuID, count) as ( -- count the number of times a student has taken a course
    SELECT course_id, ID, count(course_id)
    FROM takes
    GROUP BY ID, course_id
    ORDER BY course_id, ID
)
SELECT course, stuID -- display all course where students have taken them 3 or more times
FROM retake
WHERE count >= 3;

--@_@-- 8
WITH retake(course, stuID, count) as ( -- count the number of times a student has taken a course
    SELECT course_id, ID, count(course_id)
    FROM takes
    GROUP BY ID, course_id
    ORDER BY course_id, ID
)
SELECT foo.id
FROM (
    SELECT stuID id, count(count) c -- counts the number of courses a student has taken a course 3 times
    FROM retake
    WHERE count >= 2
    GROUP BY id
) foo
WHERE foo.c >= 3;