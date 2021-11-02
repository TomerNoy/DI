# from exercise import Dog
# import random


# class PetDog (Dog):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self):
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         print(f'{args} all play together')

#     def do_a_trick(self):
#         tricks = ['does a barrel roll', 'stands on his back legs',
#                   'shakes your hand', 'plays dead']
#         index = random.randint(0, 4)
#         print(f'{self.name} {tricks[index]}')


# sam = PetDog('sam', 7, 10)
# dan = PetDog('dan', 7, 10)
# ran = PetDog('ran', 7, 10)

# # prints None when sam.train() called right after, compiler didn't finish init?
# print(sam.trained)
# sam.train()
# print(sam.trained)

# sam.play(dan.name, ran.name, sam.name)

# sam.do_a_trick()


class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print('another one? you folks don\'t stop !')

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                if int(member['age']) >= 18:
                    return True
                else:
                    return False
        print('name doesn\'t exist')
        return False

    def get_family(self):
        print(*[member['name'] for member in self.members])


fam_members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
               {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]

fam = Family(fam_members, 'fam')
fam.born(name='Don', age=0, gender='Male', is_child=True)
print(fam.members)
print(fam.is_18('Don'))
fam.get_family()


class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self, name):
        if self.is_18(name):
            member = [member for member in self.members if member['name'] == name]
            print(member[0]['power'])
        else:
            raise Exception('not over 18')

    def incredible_presentation(self):
        print(*[member['incredible_name'] + ' | ' + member['power'] + ',' for member in self.members])


fam_members = [{'name': 'Michael', 'incredible_name': 'Mr. Incredible', 'age': 43, 'gender': 'Male', 'is_child': False, 'power': 'super-strength'},
               {'name': 'Sarah', 'incredible_name': 'Dash', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'super speed'}]

incredibles = TheIncredibles(fam_members, 'incredibles')

incredibles.get_family()
incredibles.use_power('Michael')
incredibles.incredible_presentation()
incredibles.get_family()

incredibles.born(name='Baby Jack', age=0, gender='Male', is_child=True, power = 'Unknown Power', incredible_name = 'super jack')

incredibles.incredible_presentation()
incredibles.get_family()