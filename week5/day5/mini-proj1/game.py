import random


class Game:

    hands = ["rock", "paper", "scissors"]

    def get_user_item(self):

        while True:
            hand = (input('Enter "rock", "paper" or "scissors" or "quit":\n').lower())
            if hand == 'quit':      # quit
                return None

            if hand in self.hands:  # input validation
                return hand

    def get_computer_item(self):
        return random.choice(self.hands)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:      # draw
            return 'draw'

        if user_item == "rock":
            return "win" if computer_item == "scissors" else "loss"

        if user_item == "paper":
            return "win" if computer_item == "stone" else "loss"

        if user_item == "scissors":
            return "win" if computer_item == "paper" else "loss"

    def play(self):
        '''
        the function that will be called from outside the class (ie. from rock-paper-scissors.py). 
        It will do 3 things:
            1. Get the user’s item (rock/paper/scissors) and remember it

            2. Get a random item for the computer (rock/paper/scissors) and remember it

            3. Determine the results of the game by comparing the user’s item and the computer’s item
                1. Print the output of the game; something like this: 
                    “You selected rock. The computer selected paper. You lose”, 
                    “You selected scissors. The computer selected scissors. You drew!”

                2. Return the results of the game as a string: win;draw;loss;, 
                    where win means that the user has won, draw means the user and the computer got the same item, 
                    and loss means that the user has lost.
        '''
    pass


game = Game()
# game.get_user_item()
game.get_computer_item()
