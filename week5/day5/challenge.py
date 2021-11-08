import random
import requests
import time


def test_webpage_load(url):
    start = time.time()
    requests.get(url)
    return time.time() - start


print(test_webpage_load('https://www.google.com/'))

# -------------------------------------------------

# What is a class?
# a class is an unit representing an object, item or some idea that we want to encapsulate

# What is an instance?
# instance of a class is a member of that class that has all it's variables and methods

# What is encapsulation?
# encapsulation is packing data inside the class such as variables and methods

# What is abstraction?
# abstraction is hiding encapsulated data or functions from the user

# What is inheritance?
# inheritance is inheriting data or methods from another class which can also be extended

# What is multiple inheritance?
# multiple inheritance is when a class inherits from multiple classes

# What is polymorphism?
# polymorphism is when a multiple classes inherit from the same parent class in a way they are diffrent "types" of that class

# What is method resolution order or MRO?
# MRO is the order in which a class inherits from different parents

# -------------------------------------------------

# ** not sure how/why a deck should inherit from a card, its a list of cards not a type of a card


class Card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value):
        if suit not in self.suits:
            raise Exception('invalid suit type')
        if value not in self.values:
            raise Exception('invalid value type')

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'Card: {self.value} {self.suit}\n'


class Deck():
    def __init__(self, cards):
        self.cards = []
        if type(cards) != list:
            raise Exception('only a list accepted')
        if len(cards) != 52:
            raise Exception('list count must be 52')
        for card in cards:
            if type(card) != Card:
                raise Exception('invalid type of Card in list')
        self.cards = cards

    def __repr__(self):
        return f'Deck: {self.cards}\n'

    def shuffle(self):
        unique_list = set(
            [card.value + '_' + card.suit for card in self.cards])
        if len(unique_list) != 52:
            raise Exception('not a full deck')
        random.shuffle(self.cards)

    def deal(self):
        print(f'dealing {self.cards[-1]}')
        del self.cards[-1]


cards = []
for suit in Card.suits:
    for value in Card.values:
        cards.append(Card(suit, value))

deck = Deck(cards)
deck.shuffle()
print(len(deck.cards))
deck.deal()
print(len(deck.cards))
deck.shuffle()
