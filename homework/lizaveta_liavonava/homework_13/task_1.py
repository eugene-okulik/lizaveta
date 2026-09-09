from datetime import datetime, timedelta

file_path = '/Users/lliavonova/aqa_python/lizaveta/homework/eugene_okulik/hw_13/data.txt'

with open(file_path) as file:
    for number, line in enumerate(file, start=1):
        parts = line.split(' - ')
        date = parts[0][3:]
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if number == 1:
            print(date + timedelta(weeks=1))
        elif number == 2:
            print(date.strftime('%A'))
        elif number == 3:
            print((datetime.now() - date).days)
