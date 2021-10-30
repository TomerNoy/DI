# 1,2,3
# birthdays = {
#     'dave': '2000/11/20',
#     'martin': '1980/02/11',
#     'don': '1979/05/22',
#     'chad': '1950/12/23',
#     'brandon': '2020/03/D05'
# }

# ownName = input('what\'s your name?\n')
# ownBirthday = input('what\'s your birthday in “YYYY/MM/DD” format?\n')

# birthdays[ownName] = ownBirthday

# print('welcome, you can look up the birthdays of the people on the list',
#       list(birthdays.keys()))

# name = input('enter a name:\n')
# if (name in birthdays):
#     print(f'{name}\'s birthday is on {birthdays[name]}')
# else:
#     print(f'sorry {name} not on the list')

# 4
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# sentence = ''
# for i in items:
#     sentence += (f'{i} price: {items[i]}, ')
# print(sentence[:-2] + '.')

# itemsList = [
#     {'name': "banana", 'price': 4, 'count': 1},
#     {'name': "apple", 'price': 2, 'count': 2},
#     {'name': "orange", 'price': 1.5, 'count': 10},
#     {'name': "pear", 'price': 3, 'count': 0}
# ]

# total = 0

# for i in itemsList:
#     total += i['price'] * i['count']

# print(f'sum of all fruits is {total}')

# 5,6,7
# s = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# sList = s.split(', ')
# print(sList)
# print(f'there are {len(sList)} companies in the list')
# sList.sort()
# sList.reverse()
# print(sList)
# containsCharO = [i for i in sList if "o" in i]
# notContainsCharI = [i for i in sList if "i" not in i]
# print(len(containsCharO),'|', len(notContainsCharI))

# newList = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# uniques = list(set(newList))
# print(','.join(uniques), 'total: ' ,len(uniques))

# crazy = [x[::-1] for x in uniques]
# crazy.sort()
# print(crazy)