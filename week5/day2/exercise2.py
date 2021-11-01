from exercise import Dog
import random


class PetDog (Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f'{args} all play together')

    def do_a_trick(self):
        tricks = ['does a barrel roll', 'stands on his back legs',
                  'shakes your hand', 'plays dead']
        index = random.randint(0, 4)
        print(f'{self.name} {tricks[index]}')


sam = PetDog('sam', 7, 10)
dan = PetDog('dan', 7, 10)
ran = PetDog('ran', 7, 10)

# prints None when sam.train() called right after, compiler didn't finish init?
print(sam.trained)
sam.train()
print(sam.trained)

sam.play(dan.name, ran.name, sam.name)

sam.do_a_trick()


class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print('another one? you folks don\'t stop !')

    def is_18(self):
        pass

    def get_family(self):
        pass


fam_members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
               {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]


fam = Family(fam_members, 'fam')


print(fam.members)
