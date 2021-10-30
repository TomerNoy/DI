# 1
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# for i in list2:
#     list1.append(i)


# print(list1)

# 2
# first = int(input('enter first number:\n'))
# second = int(input('enter second number:\n'))
# third = int(input('enter third number:\n'))

# print(f'the greatest is {max(first,second,third)}')

# 3
# letters = 'abcdefghijklmnopqrstuvwxyz'

# for i in letters:
#     isVowel = False
#     if i in 'aeiou':
#         isVowel = True
#     print(f'{i} is{"" if isVowel else " not"} a vowel')

# 4
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# ask = input('enter your name:\n')

# if ask in names:
#     print(names.index(ask))

# 5
# words = (input('please enter 7 words seperated by space:\n')).split(',')
# letter = input('please enter 1 character:\n')

# for i in words:
#     if letter in i:
#         print(i.index(letter))
#     else:
#         print(f'sorry {letter} is\'t in {i}')

# 6
# list = range(1, 1000000)
# print(min(list), max(list), sum(list))

# 7
# nums = input('please enter numbers seperated by comma:\n')

# listIs =  nums.split(',')
# tupleIs = tuple(listIs)
# print(listIs, tupleIs)

# 8

# import random

# won = 0
# lost = 0

# while True:
#     num = input('enter a number from 1 - 9, to quite enter "quit":\n')
#     if num == 'quit':
#         break
#     ran = random.randint(1, 9)
#     if (num == str(ran)):
#         won += 1
#         print('Winner')
#     else:
#         lost += 1
#         print('better luck next time.')
# print(f'you won {won} times and lost {lost} times')
