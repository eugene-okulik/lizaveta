def process_text(text):
    pieces = text.split(':')
    number = int(pieces[1])
    print(number + 10)

texts = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

for current_text in texts:
    process_text(current_text)
