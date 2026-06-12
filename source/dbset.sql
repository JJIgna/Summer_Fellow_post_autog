-- create user testee
CREATE USER testee WITH PASSWORD 'pass' SUPERUSER;
CREATE DATABASE testee;

-- moving into testee db
\c testee

-- db setup
create table classroom 
	(building		varchar(15),
	 room_number		varchar(7),
	 capacity		numeric(4,0),
	 primary key (building, room_number)
	);

ALTER TABLE classroom OWNER TO testee;

create table department
	(dept_name		varchar(20),
	 building		varchar(15),
	 budget		        numeric(12,2) check (budget > 0),
	 primary key (dept_name)
	);

ALTER TABLE department OWNER TO testee;

create table course
	(course_id		varchar(8),
	 title			varchar(50),
	 dept_name		varchar(20),
	 credits		numeric(2,0) check (credits > 0),
	 primary key (course_id),
	 foreign key (dept_name) references department (dept_name)
		on delete set null
	);

ALTER TABLE course OWNER TO testee;

create table instructor
	(ID			varchar(5),
	 name			varchar(20) not null,
	 dept_name		varchar(20),
	 salary			numeric(8,2) check (salary > 29000),
	 primary key (ID),
	 foreign key (dept_name) references department (dept_name)
		on delete set null
	);

ALTER TABLE instructor OWNER TO testee;

create table time_slot
	(time_slot_id		varchar(4),
	 day			varchar(1),
	 start_hr		numeric(2) check (start_hr >= 0 and start_hr < 24),
	 start_min		numeric(2) check (start_min >= 0 and start_min < 60),
	 end_hr			numeric(2) check (end_hr >= 0 and end_hr < 24),
	 end_min		numeric(2) check (end_min >= 0 and end_min < 60),
	 primary key (time_slot_id, day, start_hr, start_min)
	);

ALTER TABLE time_slot OWNER TO testee;

create table section
	(course_id		varchar(8),
     sec_id			varchar(8),
	 semester		varchar(6)
		check (semester in ('Fall', 'Winter', 'Spring', 'Summer')),
	 year			numeric(4,0) check (year > 1701 and year < 2100),
	 building		varchar(15),
	 room_number		varchar(7),
	 time_slot_id		varchar(4),
	 primary key (course_id, sec_id, semester, year),
	 foreign key (course_id) references course (course_id)
		on delete cascade,
	 foreign key (building, room_number) references classroom (building, room_number)
		on delete set null
	);

ALTER TABLE section OWNER TO testee;

create table teaches
	(ID			varchar(5),
	 course_id		varchar(8),
	 sec_id			varchar(8),
	 semester		varchar(6),
	 year			numeric(4,0),
	 primary key (ID, course_id, sec_id, semester, year),
	 foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year)
		on delete cascade,
	 foreign key (ID) references instructor (ID)
		on delete cascade
	);

ALTER TABLE teaches OWNER TO testee;

create table student
	(ID			varchar(5),
	 name			varchar(20) not null,
	 dept_name		varchar(20),
	 tot_cred		numeric(3,0) check (tot_cred >= 0),
	 primary key (ID),
	 foreign key (dept_name) references department (dept_name)
		on delete set null
	);

ALTER TABLE student OWNER TO testee;

create table takes
	(ID			varchar(5),
	 course_id		varchar(8),
	 sec_id			varchar(8),
	 semester		varchar(6),
	 year			numeric(4,0),
	 grade		        varchar(2),
	 primary key (ID, course_id, sec_id, semester, year),
	 foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year)
		on delete cascade,
	 foreign key (ID) references student (ID)
		on delete cascade
	);

ALTER TABLE takes OWNER TO testee;

create table advisor
	(s_ID			varchar(5),
	 i_ID			varchar(5),
	 primary key (s_ID),
	 foreign key (i_ID) references instructor (ID)
		on delete set null,
	 foreign key (s_ID) references student (ID)
		on delete cascade
	);

ALTER TABLE advisor OWNER TO testee;

create table prereq
	(course_id		varchar(8),
	 prereq_id		varchar(8),
	 primary key (course_id, prereq_id),
	 foreign key (course_id) references course (course_id)
		on delete cascade,
	 foreign key (prereq_id) references course (course_id)
	);

ALTER TABLE prereq OWNER TO testee;

-- populate

BEGIN;

-- departments
INSERT INTO department (dept_name, building, budget) VALUES
('Comp. Sci.', 'Taylor', 900000.00),
('Biology', 'Watson', 700000.00),
('Elec. Eng.', 'Packard', 800000.00),
('Physics', 'Watson', 650000.00),
('Finance', 'Painter', 500000.00),
('History', 'Painter', 400000.00),
('Music', 'Taylor', 300000.00);

-- classrooms
INSERT INTO classroom (building, room_number, capacity) VALUES
('Taylor', '100', 50),
('Taylor', '101', 30),
('Taylor', '102', 40),
('Watson', '201', 40),
('Watson', '202', 35),
('Watson', '203', 50),
('Packard', '101', 60),
('Packard', '102', 45),
('Painter', '110', 50),
('Painter', '111', 25);

-- courses
INSERT INTO course (course_id, title, dept_name, credits) VALUES
('CS-101', 'Intro. to Computer Science', 'Comp. Sci.', 4),
('CS-190', 'Game Design', 'Comp. Sci.', 4),
('CS-315', 'Robotics', 'Comp. Sci.', 3),
('CS-347', 'Database System Concepts', 'Comp. Sci.', 3),
('BIO-101', 'Intro. to Biology', 'Biology', 4),
('BIO-301', 'Genetics', 'Biology', 4),
('EE-181', 'Intro. to Electrical Eng.', 'Elec. Eng.', 3),
('EE-301', 'Signals and Systems', 'Elec. Eng.', 3),
('PHY-101', 'Physical Principles', 'Physics', 4),
('PHY-201', 'Physics II', 'Physics', 4),
('FIN-201', 'Corporate Finance', 'Finance', 3),
('FIN-301', 'Investment Strategies', 'Finance', 3),
('HIS-101', 'World History', 'History', 3),
('HIS-201', 'US History', 'History', 3),
('MUS-101', 'Music Theory', 'Music', 3);

-- instructors
INSERT INTO instructor (ID, name, dept_name, salary) VALUES
('10101', 'Srinivasan', 'Comp. Sci.', 95000.00),
('10102', 'Mozart', 'Music', 72000.00),
('12121', 'Wu', 'Finance', 90000.00),
('15151', 'Einstein', 'Physics', 95000.00),
('22222', 'Gold', 'Biology', 80000.00),
('32343', 'El Said', 'History', 60000.00),
('45565', 'Katz', 'Comp. Sci.', 75000.00),
('58583', 'Califieri', 'History', 62000.00),
('76543', 'Singh', 'Finance', 80000.00),
('76766', 'Crick', 'Biology', 72000.00),
('83821', 'Brandt', 'Comp. Sci.', 92000.00),
('98345', 'Kim', 'Elec. Eng.', 80000.00);

-- time slots
INSERT INTO time_slot (time_slot_id, day, start_hr, start_min, end_hr, end_min) VALUES
('A', 'M', 8, 0, 9, 30),
('A', 'W', 8, 0, 9, 30),
('B', 'T', 9, 0, 10, 30),
('B', 'R', 9, 0, 10, 30),
('C', 'M', 11, 0, 12, 30),
('C', 'W', 11, 0, 12, 30),
('D', 'T', 13, 0, 14, 30),
('D', 'R', 13, 0, 14, 30),
('E', 'F', 10, 0, 11, 30),
('F', 'M', 14, 0, 15, 30),
('F', 'W', 14, 0, 15, 30),
('G', 'T', 15, 0, 16, 30),
('G', 'R', 15, 0, 16, 30);

-- sections (Fall 2023 and Spring 2024)
INSERT INTO section (course_id, sec_id, semester, year, building, room_number, time_slot_id) VALUES
('CS-101', '1', 'Fall', 2023, 'Taylor', '100', 'A'),
('CS-101', '1', 'Spring', 2024, 'Taylor', '100', 'B'),
('CS-190', '1', 'Spring', 2024, 'Taylor', '102', 'C'),
('CS-315', '1', 'Fall', 2023, 'Taylor', '101', 'D'),
('CS-347', '1', 'Fall', 2023, 'Taylor', '101', 'F'),
('BIO-101', '1', 'Fall', 2023, 'Watson', '201', 'A'),
('BIO-301', '1', 'Spring', 2024, 'Watson', '202', 'B'),
('EE-181', '1', 'Spring', 2024, 'Packard', '101', 'C'),
('EE-301', '1', 'Fall', 2023, 'Packard', '102', 'D'),
('PHY-101', '1', 'Fall', 2023, 'Watson', '203', 'E'),
('PHY-201', '1', 'Spring', 2024, 'Watson', '203', 'F'),
('FIN-201', '1', 'Fall', 2023, 'Painter', '110', 'A'),
('FIN-301', '1', 'Spring', 2024, 'Painter', '110', 'G'),
('HIS-101', '1', 'Fall', 2023, 'Painter', '111', 'B'),
('MUS-101', '1', 'Spring', 2024, 'Taylor', '102', 'D');

-- teaches
INSERT INTO teaches (ID, course_id, sec_id, semester, year) VALUES
('10101', 'CS-101', '1', 'Fall', 2023),
('45565', 'CS-101', '1', 'Spring', 2024),
('83821', 'CS-190', '1', 'Spring', 2024),
('10101', 'CS-315', '1', 'Fall', 2023),
('83821', 'CS-347', '1', 'Fall', 2023),
('22222', 'BIO-101', '1', 'Fall', 2023),
('76766', 'BIO-301', '1', 'Spring', 2024),
('98345', 'EE-181', '1', 'Spring', 2024),
('98345', 'EE-301', '1', 'Fall', 2023),
('15151', 'PHY-101', '1', 'Fall', 2023),
('15151', 'PHY-201', '1', 'Spring', 2024),
('12121', 'FIN-201', '1', 'Fall', 2023),
('76543', 'FIN-301', '1', 'Spring', 2024),
('32343', 'HIS-101', '1', 'Fall', 2023),
('10102', 'MUS-101', '1', 'Spring', 2024);

-- students
INSERT INTO student (ID, name, dept_name, tot_cred) VALUES
('00128', 'Zhang', 'Comp. Sci.', 102),
('12345', 'Shankar', 'Comp. Sci.', 32),
('19991', 'Brandt', 'History', 80),
('23121', 'Chavez', 'Finance', 110),
('44553', 'Peltier', 'Physics', 56),
('45678', 'Levy', 'Physics', 46),
('54321', 'Williams', 'Comp. Sci.', 54),
('55739', 'Sanchez', 'Music', 38),
('76543', 'Brown', 'Comp. Sci.', 58),
('76653', 'Aoi', 'Elec. Eng.', 60),
('98765', 'Bourikas', 'Elec. Eng.', 98),
('98988', 'Tanaka', 'Biology', 120),
('00123', 'Lam', 'Finance', 72),
('23456', 'Johnson', 'History', 40),
('34567', 'Smith', 'Biology', 88);

-- advisor
INSERT INTO advisor (s_ID, i_ID) VALUES
('00128', '10101'),
('12345', '45565'),
('19991', '32343'),
('23121', '12121'),
('44553', '15151'),
('45678', '15151'),
('54321', '83821'),
('55739', '10102'),
('76543', '10101'),
('76653', '98345'),
('98765', '98345'),
('98988', '22222'),
('00123', '76543'),
('23456', '58583'),
('34567', '76766');

-- takes
INSERT INTO takes (ID, course_id, sec_id, semester, year, grade) VALUES
('00128', 'CS-101', '1', 'Fall', 2023, 'A'),
('00128', 'CS-347', '1', 'Fall', 2023, 'A-'),
('12345', 'CS-101', '1', 'Fall', 2023, 'C'),
('12345', 'CS-190', '1', 'Spring', 2024, 'B+'),
('12345', 'CS-315', '1', 'Fall', 2023, 'A'),
('19991', 'HIS-101', '1', 'Fall', 2023, 'B'),
('23121', 'FIN-201', '1', 'Fall', 2023, 'A-'),
('23121', 'FIN-301', '1', 'Spring', 2024, 'B+'),
('44553', 'PHY-101', '1', 'Fall', 2023, 'B'),
('44553', 'PHY-201', '1', 'Spring', 2024, 'A-'),
('45678', 'PHY-101', '1', 'Fall', 2023, 'C+'),
('54321', 'CS-101', '1', 'Fall', 2023, 'A'),
('54321', 'CS-190', '1', 'Spring', 2024, 'A'),
('55739', 'MUS-101', '1', 'Spring', 2024, 'A-'),
('76543', 'CS-101', '1', 'Spring', 2024, 'B'),
('76543', 'CS-347', '1', 'Fall', 2023, 'B+'),
('76653', 'EE-181', '1', 'Spring', 2024, 'A'),
('98765', 'EE-181', '1', 'Spring', 2024, 'C'),
('98765', 'EE-301', '1', 'Fall', 2023, 'B'),
('98988', 'BIO-101', '1', 'Fall', 2023, 'A'),
('98988', 'BIO-301', '1', 'Spring', 2024, 'A'),
('00123', 'FIN-201', '1', 'Fall', 2023, 'B'),
('23456', 'HIS-101', '1', 'Fall', 2023, 'A-'),
('34567', 'BIO-101', '1', 'Fall', 2023, 'B+'),
('34567', 'BIO-301', '1', 'Spring', 2024, 'B');

-- prerequisites
INSERT INTO prereq (course_id, prereq_id) VALUES
('CS-190', 'CS-101'),
('CS-315', 'CS-101'),
('CS-347', 'CS-101'),
('BIO-301', 'BIO-101'),
('EE-301', 'EE-181'),
('PHY-201', 'PHY-101'),
('FIN-301', 'FIN-201'),
('CS-315', 'PHY-101');

COMMIT;