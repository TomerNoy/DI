# 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# d = {}
# for i, j in zip(keys, values):
#     d[i] = j
# print(d)

# 2
# family = {}
# name = input(f'Please enter your name:\n')
# age = input(f'Hi, {name} how old are you?\n')
# family[name] = int(age)

# while 1:
#     newName = input(
#         'Do you have another family member? please enter his name or enter "quit":\n')
#     if (newName == 'quit'):
#         break
#     age = input(f'how old is {newName}:\n')
#     family[newName] = int(age)
# total = 0
# for v in family.values():
#     if 3 <= v < 12:
#         total += 10
#     elif v >= 12:
#         total += 15
# print(f'total price is {total}')

# 3
# brand = {
#     'name': 'Zara ',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'],
#     'number_stores': 7000,
#     'major_color': {'France': 'blue', 'Spain': 'red', 'US': 'green'}
# }

# brand['number_stores'] = 2

# type_of_clothes = brand["type_of_clothes"]
# clients = ''
# for i, v in enumerate(type_of_clothes):
#     if i == 0:
#         clients = v
#     elif i < len(type_of_clothes)-1:
#         clients += ' ,' + v
#     else:
#         clients += ' and ' + v
# print(f'zara\'s cloths are made for {clients}')

# brand['country_creation'] = 'Spain'

# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')

# if 'creation_date' in brand:
#     del brand['creation_date']

# print(brand['international_competitors'][-1])

# print(brand['major_color']['US'])

# print(len(brand))

# print(list(brand.keys()))

# more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

# for k,v in more_on_zara.items():
#     brand[k] = v

# print(brand['number_stores']) #number_stores got replaced

# 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
for k, v in enumerate(users):
    disney_users_A[v] = k
print(disney_users_A)

disney_users_B = {}
for k, v in enumerate(users):
    disney_users_B[k] = v
print(disney_users_B)

disney_users_C = {}
for k, v in enumerate(sorted(users)):
    disney_users_C[v] = k
print(disney_users_C)


disney_users_AX = {}
for k, v in enumerate(users):
    if ('i' in v and (v[0] == 'M' or v[0] == 'P')):
        disney_users_AX[v] = k
print(disney_users_AX)