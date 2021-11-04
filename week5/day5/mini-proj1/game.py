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
            return 'draw!'

        if user_item == "rock":
            return "win!" if computer_item == "scissors" else "loss"

        if user_item == "paper":
            return "win!" if computer_item == "stone" else "loss"

        if user_item == "scissors":
            return "win!" if computer_item == "paper" else "loss"

    def play(self):
        hand = self.get_user_item()
        if hand == None:
            print('Goodbye !')
            return

        com_hand = self.get_computer_item()

        result = self.get_game_result(hand, com_hand)

        print(
            f'You selected {hand}. The computer selected {com_hand}. You {result}')
        return result


game = Game()
game.play()
# game.get_user_item()
# game.get_computer_item()
