# 2
import random


def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    d1 = throw_dice()
    d2 = throw_dice()
    count = 0
    while d1 != d2:
        count+= 1
    
