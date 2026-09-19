import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)
cursor = db.cursor(dictionary=True)
cursor.execute('select * from students')
data = cursor.fetchall()
# print(data)


cursor.execute(
    "insert into students (name, second_name) values (%s, %s)",
    ('Donna', 'Tartt')
)
student_id = cursor.lastrowid
print('student_id:', student_id)


cursor.executemany(
    "insert into books (title, taken_by_student_id) values (%s, %s)",
    [
        ('The Secret History', student_id),
        ('The Goldfinch', student_id),
        ('The Little Friend', student_id),
    ]
)

cursor.execute(
    "SELECT id, title FROM books WHERE taken_by_student_id = %s",
    (student_id,)
)

print("Student's books:")
for row in cursor.fetchall():
    print(row)


cursor.execute(
    "insert into `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('readers', 'apr 2026', 'dec 2026')
)
group_id = cursor.lastrowid

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
print('group_id:', group_id)

cursor.execute(
    "INSERT INTO subjects (title) VALUES (%s)",
    ('french - donna',))
french_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO subjects (title) VALUES (%s)",
    ('english - donna',))
english_id = cursor.lastrowid

print('French ID:', french_id, 'English ID:', english_id)

query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

cursor.execute(query, ('french - donna: basics', french_id))
lesson_1 = cursor.lastrowid

cursor.execute(query, ('french - donna: grammar', french_id))
lesson_2 = cursor.lastrowid

cursor.execute(query, ('english - donna: basics', english_id))
lesson_3 = cursor.lastrowid

cursor.execute(query, ('english - donna: grammar', english_id))
lesson_4 = cursor.lastrowid

print('Lesson IDs:', lesson_1, lesson_2, lesson_3, lesson_4)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"

cursor.execute(query, (10, lesson_1, student_id))
cursor.execute(query, (5, lesson_2, student_id))
cursor.execute(query, (79, lesson_3, student_id))
cursor.execute(query, (5, lesson_4, student_id))

cursor.execute("SELECT value FROM marks WHERE student_id = %s",
               (student_id,))
print('\nMarks:')
for row in cursor.fetchall():
    print(row)

cursor.execute("""
     SELECT
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
     where s.id = %s
""", (student_id,))

print('\nEverything about the student:')
for row in cursor.fetchall():
    print(row)

db.commit()
cursor.close()
db.close()
