# 1
# my_fav_numbers = {3, 999, 5}
# my_fav_numbers.add(4)
# my_fav_numbers.add(9)
# my_fav_numbers.remove(9)
# friend_fav_numbers = {3, 54, 56}
# our_fav_numbers = my_fav_numbers | friend_fav_numbers
# print(our_fav_numbers)

# 2
# tuples are immutable - they can’t be changed


# 3
# for i in range(1, 21):
#     print(i)

# 4
# float has a decimal and int doesn't

# floatList1 = []
# for i in range(1, 10):
#     floatList1.append(float(i))
#     floatList1.append(i+0.5)

# floatList2 = []
# for i in range(2, 6):
#     floatList2.append(i-0.5)
#     floatList2.append(i)

# 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# 6
# myName = 'tom'
# ask = input('whats your name?')
# while ask != myName:
#     ask = input('whats your name again?')

# 7
# some_list = [23, 4, 56, 7, 90, 11]
# for i in range(0, len(some_list)):
#     if i % 2 == 0:
#         print(some_list[i])

# 8
# for i in range(1500, 2500):
#     if i % 35 == 0:
#         print(i)

# 9
# fruits = input("enter fruits seperated by \",\":")
# list = fruits.split(',')
# fruit = input("enter some fruit name:")
# if fruit in fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# 10
# toppings = []
# topping = input('enter a pizza topping:')

# while topping != 'quit':
#     toppings.append(topping)
#     print(f'we\'ll add {topping} to the pizza')
#     topping = input('enter another pizza topping:')

# total = 10 + 2.5 * len(toppings)
# print(f'total price is {total}')

# 11
# prices = []
# family_count = input('how many members in your family?')
# for i in range(0, int(family_count)):
#     age = int(input(f'please enter the {i+1}th member age:'))
#     if age < 3:
#         print('ticket is free')
#     elif age < 13:
#         print('ticket is $10')
#         prices.append(10)
#     else:
#         print('ticket is $15')
#         prices.append(15)
# print(sum(prices))

# permitted = []
# count = input('how many are you?')
# print('please answer one by one')
# for i in range(0, int(count)):
#     name = input('what\'s your name?')
#     age = int(input('how old are you?'))
#     if 21 >= age >= 16:
#         permitted.append(name)
#     if (i < int(count)):
#         print('next one please')
# print(f'the following can enter: {permitted}')

# 12
# names = ['name1', 'name2', 'name3']
# namesOK = names.copy()

# for i in range(0, len(names)):
#     print(i)
#     age = int(input(f'{names[i]} how old are you?'))
#     if age < 16:
#         namesOK.remove(names[i])
# print(namesOK)

# 13
# 14
# sandwich_orders = ['Egg Sandwich', 'Pastrami Sandwich',
#                    'Seafood Sandwich', 'Pastrami Sandwich', 'Nutella Sandwich', 'Pastrami Sandwich']
# finished_sandwiches = []
# print('we run out of pastrami')

# while 'Pastrami Sandwich' in sandwich_orders:
#     sandwich_orders.remove('Pastrami Sandwich')

# for i in range(0, len(sandwich_orders)):
#     finished_sandwiches.append(sandwich_orders[i])
#     print(f'I made your {sandwich_orders[i]}')
# print(finished_sandwiches)

