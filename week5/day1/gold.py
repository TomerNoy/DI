import random
import math


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def geometrical_definition(self):
        print('A circle is a plane figure bounded by one curved line, and such that all straight lines drawn from a certain point within it to the bounding line, are equal. The bounding line is called its circumference and the point, its centre.')


circle1 = Circle()
circle2 = Circle(1.5)

print(circle1.perimeter())
print(circle2.area())
circle1.geometrical_definition()


class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        return list(reversed(self.letters))

    def sorted_list(self):
        return sorted(self.letters)

    def gen_random(self):
        return [random.randint(0, 100) for i in range(len(self.letters))]


list1 = MyList(['a', 't', 'c'])
print(list1.reversed_list())
print(list1.sorted_list())
print(list1.gen_random())


class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        for item in self.menu:
            if name == item['name']:
                print('already exists')
                return
        self.menu.append(
            {
                'name': name,
                'price': price,
                'spice': spice,
                'gluten': gluten,
            }
        )

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if name == item['name']:
                item[price] = price
                item[spice] = spice
                item[gluten] = gluten
                return
        print('not in the menu')

    def remove_item(self, name):
        for item in self.menu:
            if name == item['name']:
                self.menu.remove(item)
                print(self.menu)
                return
        print('not in the menu')


dave = MenuManager()
dave.add_item('Soup', 10, 'B', False)
dave.add_item('Hamburger', 12, 'B', True)
dave.add_item('Hamburger', 12, 'B', True)
dave.add_item('Salad', 13, 'A', False)
dave.add_item('Beef bourguignon', 10, 'D', False)

dave.remove_item('Hamburger')

print(dave.menu)
