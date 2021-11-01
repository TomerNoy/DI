class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Zulu(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Cat('slayer', 6)
cat2 = Cat('riper', 2)
cat3 = Cat('jack', 3)

cats = [cat1, cat2, cat3]

my_pets = Pets(cats)

my_pets.walk()


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):

        if (self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight):
            winner =  self
        else:
            winner =  other_dog
        print(f'{winner.name} won the fight')
    

dog1 = Dog('box', 8, 20)
dog2 = Dog('rex', 6, 18 )
dog3 = Dog('rex', 6, 18 )

dog1.fight(dog2)


