SELECT *
FROM students;

insert into students (name, second_name) 
values ('Donna', 'Tartt');



select students.id 
from students 
where name = 'Donna' and second_name = 'Tartt';


select *
from books;

insert into books (title, taken_by_student_id)
values ('The Secret History', 23199), ('The Goldfinch', 23199), ('The Little Friend', 23199);



select *
from `groups`;

insert into `groups` (title, start_date, end_date)
values ('readers', 'apr 2026', 'dec 2026');

update students s
join `groups` g 
on g.title = 'readers'
set s.group_id = g.id 
where s.name = 'Donna' AND s.second_name = 'Tartt';



select *
from subjects;

insert into subjects (title)
values ('french - donna'), ('english - donna');


select *
from subjects 
where title in ('french - donna', 'english - donna');

select *
from lessons;

insert into lessons (title, subject_id)
values 
	('french - donna: basics', 23423),
	('french - donna: grammar', 23423),
	('english - donna: basics', 23424),
	('english - donna: grammar', 23424);

select *
from lessons
where title in ('french - donna: basics', 'french - donna: grammar', 'english - donna: basics', 'english - donna: grammar');

	
select * 
from marks;

insert into marks (value, lesson_id, student_id)
values 
	('10', 76918, 23199),
	('5', 76919, 23199),
	('79', 76920, 23199),
	('5', 76921, 23199);




select value
from marks 
where student_id = 23199;

select title 
from books 
where taken_by_student_id = 23199;



select 
	s.id AS student_id, 
	s.name,
	s.second_name,
	g.id AS group_id,
	g.title AS group_title,
	g.start_date,
	g.end_date,
	b.id AS book_id,
	b.title AS book_title,
	sub.title           AS subject_title,
    l.title             AS lesson_title,
    m.value             AS mark	
from students s
left join books b
ON s.id = b.taken_by_student_id
left join `groups` g 
on s.group_id = g.id 
left join marks m
on s.id = m.student_id
left join lessons l
on l.id   = m.lesson_id
left join subjects sub
on sub.id = l.subject_id
where s.id = 23199;




