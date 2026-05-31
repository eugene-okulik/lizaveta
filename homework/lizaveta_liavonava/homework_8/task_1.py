import random
salary = int(input('Please enter your salary: '))
bonus = random.choice([True, False])
if bonus:
    bonus_amount = random.randint(1000, 10000)
    total = salary + bonus_amount
    print(f'{salary}, {bonus} - ${total}')
else:
    print(f'{salary}, {bonus} - ${salary}')
          