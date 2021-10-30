# 1
# import random

# randomLength = random.randint(50, 1000)
# print(randomLength)

# listN = [random.randint(-100, 100) for i in range(randomLength)]

# while len(listN) < 11:
#     num = input('enter a number between -100 to 100:\n')
#     print(num.isnumeric())
#     if num.isnumeric():
#         num = int(num)
#         if -100 < num < 100:
#             listN.append(num)


# print(listN)
# sortedList = sorted(listN)
# sortedList.reverse()
# print(sortedList)
# print(sum(sortedList))
# print(listN[0], listN[len(listN) - 1])

# greater50 = []
# for n in listN:
#     if n > 50:
#         greater50.append(n)
# print(greater50)

# smaller10 = []
# for n in listN:
#     if n < 10:
#         smaller10.append(n)
# print(smaller10)
# sqrd = []
# for n in listN:
#     sqrd.append(n**2)
# print(sqrd)

# originals = list(set(listN))
# print(originals, f'total of {len(originals)}')
# print(int(sum(listN) / len(listN)))
# print(max(listN), min(listN))

# # bonus
# sum = 0
# totalVals = 0
# avarage = 0
# largest = 0
# smallest = 0
# for i in listN:
#     totalVals += 1
#     sum += i
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# avarage = int(sum / totalVals)
# print(sum, avarage, largest, smallest)

# 2,3
# accounts = {
#     'dan': '123',
#     'jack': '234',
#     'bob': '345',
# }

# logged_in = ''

# while True:
#     login = input('enter "login" or "exit":\n')
#     if login == 'exit':
#         break
#     elif login == 'login':
#         name = input('username:\n')
#         pwd = input('password:\n')
#         if name in accounts:
#             if accounts[name] == pwd:
#                 logged_in = [name, pwd]
#                 print('You\'re logged In')
#                 break
#         sign = input('user doesn\'t exist would you like to sign up? y/n\n')
#         if sign == 'y':
#             username = input('enter username:\n')
#             while username in accounts:
#                 username = input('username already exists, try another:\n')
#             password = input('enter password:\n')
#             accounts[username] =password
#             logged_in = [username, password]
#             print('Added and Logged In')
#             break

