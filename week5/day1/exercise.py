class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1. 2
riper = Cat('riper', '6')
slayer = Cat('slayer', '8')


def oldest_cat(cat_list):
    oldest = sorted(cat_list, key=lambda cat: cat.age, reverse=True)[0]
    print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')


oldest_cat([riper, slayer])

# 2


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {int(self.height) * 2} cm high!')


davids_dog = Dog('davids_dog', '50')
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', '20')
print(sarahs_dog.name, davids_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if int(sarahs_dog.height) > int(davids_dog.height):
    print('sarahs_dog is bigger')
else:
    print('davids_dog is bigger')

# 3


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for s in self.lyrics:
            print(s)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# 4


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.pop(self.animals.index(animal_sold))

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        count = 1
        while len(sorted_animals) > 0:
            first_animal = sorted_animals.pop(0)
            animals = [first_animal]
            for animal in sorted_animals:
                if animal[0] == first_animal[0]:
                    animals.append(animal)
                    sorted_animals.remove(animal)
            if len(animals) == 1:
                self.groups[count] = animals[0]
            else:
                self.groups[count] = animals
            count += 1

    def get_groups(self):
        print(self.groups)


ramat_gan_safari = Zoo('ramat_gan_safari')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Emu')

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()

