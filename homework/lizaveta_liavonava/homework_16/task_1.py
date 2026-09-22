import mysql.connector as mysql
import os
import dotenv
import csv

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', '..', 'eugene_okulik', 'Lesson_16', '.env')
dotenv.load_dotenv(file_path)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)


cursor = db.cursor(dictionary=True)
cursor.execute('SHOW TABLES')
data = cursor.fetchall()
print(data)

for table_name in data:
    name = table_name['Tables_in_st-onl']
    cursor.execute(f'DESCRIBE `{name}`')
    data_1 = cursor.fetchall()
    print(data_1)

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
""", )
db_data = cursor.fetchall()
for row in db_data:
    print(row)

cursor.close()
db.close()


file_path_1 = os.path.join(base_path, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
with (open(file_path_1, newline='', encoding='utf-8') as csv_file):
    file_data = csv.DictReader(csv_file)
    csv_data = []
    for row in file_data:
        csv_data.append(row)

    for row_csv in csv_data:
        for row_db in db_data:
            if (row_csv['name'] == row_db['name']
                    and row_csv['second_name'] == row_db['second_name']
                    and row_csv['group_title'] == row_db['group_title']
                    and row_csv['book_title'] == row_db['book_title']
                    and row_csv['subject_title'] == row_db['subject_title']
                    and row_csv['lesson_title'] == row_db['lesson_title']
                    and row_csv['mark_value'] == str(row_db['mark'])
                ):
                break
        else:
            print('Data not found:', row_csv)
