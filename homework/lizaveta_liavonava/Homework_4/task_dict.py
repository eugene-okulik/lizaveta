my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {'a': 'cat', 'b': 'dog', 'c': 'mouse', 'd': 'kitten', 'e': 'puppy'},
    'set': {'10', '20', '30', '40', '50'}
}
#tuple: выведите на экран последний элемент
print('tuples last element: ', my_dict['tuple'][-1])

#list: добавьте в конец списка еще один элемент; удалите второй элемент списка
my_dict['list'].append('six')
del my_dict['list'][1]

#dict: добавьте элемент с ключом ('i am a tuple',) и любым значением; удалите какой-нибудь элемент
my_dict['dict']['i am a tuple'] = 'me'
del my_dict['dict']['a']

#set: добавьте новый элемент в множество; удалите элемент из множества
my_dict['set'].add('35')
my_dict['set'].discard('35')

#whole dict
print(my_dict)