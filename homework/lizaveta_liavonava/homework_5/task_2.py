text ='результат операции: 42'
digit = int(text[text.index(':') + 2:])
print(digit + 10)
text = 'результат операции: 514'
digit = int(text[text.index(':') + 2:])
print(digit + 10)
text = 'результат работы программы: 9'
digit = int(text[text.index(':') + 2:])
print(digit + 10)
