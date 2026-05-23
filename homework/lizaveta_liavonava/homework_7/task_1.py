secret_number = 7
user_input = int(input('Введите число: '))

while user_input != secret_number:
        print('попробуйте снова')
        user_input = int(input('Введите число: '))

print('Поздравляю! Вы угадали!')
