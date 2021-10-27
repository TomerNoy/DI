import random
# 1


def display_message():
    print('hi everyone i\'m learning in developers institute')


display_message()

# 2


def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('Alice in Wonderland')

# 3


def describe_city(city, country='Israel'):
    print(f'{city} is in {country}')


describe_city('Tel Aviv')

# 4


def myRandom(num):
    newRandom = random.randint(1, 100)
    if newRandom == num:
        print('success')
    else:
        print('fail', num, newRandom)


myRandom(12)

# 5


def make_shirt(size='large', msg='I love Python'):
    print(f'the message "{msg}"" will be printed on a {size} sized shirt')


make_shirt('small', 'DI for life')
make_shirt('large')
make_shirt('medium')
make_shirt('medium', 'DI for life')

make_shirt(size='small', msg='unicorns')

# 6
magicians = ['zorgo', 'mentus', 'tampta']


def show_magicians(list):
    for i in list:
        print(i)


show_magicians(magicians)


def make_great(magicians):
    return [x + ' the grate' for x in magicians]


magicians = make_great(magicians)

show_magicians(magicians)
