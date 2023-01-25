# idea : BLACKJACK GAME
from computer import opponent
from player import game
# from finish import ending
from random import randint

print("Welcome to Blackjack, your goal is to hit 21, however, if you go over it, you lose.")
print("Here are your starting cards")
print("*Note that jokers and royals are exlcuded from deck for quick play!*")
print(" ")
# Player variables
card1 = randint(1,11)
card2 = randint(1,11)
choices = ["hit","stand"]
hand = card1 + card2

# computer variables
computer_card1 = randint(1,11)
computer_card2 = randint(1,11)
computer_hand = computer_card1 + computer_card2

computer_play=opponent(computer_card1,computer_card2, computer_hand)
play=game(card1,card2,hand,choices)

print(" ")
print("Whoever got closer to 21 WINS!")
print("If computer busted, you Win!")
print("However, if you also busted you Lose!")




