
# part 2 question 1 seems like a mistake to me because of:
#   - mismatch function name vs porpoise
#   - creating an instance of menuItem without it's init content
#
# changing "load_manager" with "update_item" because it was missing from part 2

from exercise import MenuItem
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'tomernoy'
PASSWORD = '#'
DATABASE = 'restaurant'


connection = psycopg2.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE
)


def show_user_menu():
    # displays the program menu
    while True:
        i = input(
            '''
    MENU
(a) Add an item
(d) Delete an item
(u) Update an item
(v) View the menu
(x) Exit
:''')

        # add
        if i == 'a':
            while True:
                title = input('Enter title:\n')
                price = input(f'Enter price for {title}:\n')
                while not price.isnumeric:
                    price = input('Invalid price, please try again:\n')
                return add_item_to_menu(title, price)

        # delete
        elif i == 'd':
            while True:
                title = input('Enter title:\n')
                return remove_item_from_menu(title)

        # update
        elif i == 'u':
            while True:
                i = input('Enter title:\n')
                item = MenuItem.get_by_name(i, connection)
                if item == None:
                    print(f'Sorry, {i} not found')
                    return show_user_menu()
                return update_item(item)

        # view menu
        elif i == 'v':
            show_restaurant_menu()

        # exit
        elif i == 'x':
            break
        else:
            print('invalid input try again?')


def add_item_to_menu(title, price):
    item = MenuItem(title, price, connection)
    item.save()
    return show_user_menu()


def remove_item_from_menu(title):
    item = MenuItem.get_by_name(title, connection)
    if (item == None):
        print('Somthing went wrong, this item doesn\'t exit')
    else:
        item.delete()
    return show_user_menu()


def update_item(item):
    while True:
        title = input(
            'Enter the new name or leave empty for default:\n')
        if title == '':
            title = item.title

        price = input(
            f'Enter new price for {title} or leave empty for default:\n')
        if price == '':
            price = item.price
        else:
            while not price.isnumeric:
                price = input('Invalid price, please try again:\n')
        # print('->',title, price)
        item.update(title, price)
        return show_user_menu()


def show_restaurant_menu():
    MenuItem.all(connection)


show_user_menu()
connection.close()
# exit()