from random import randint
import random

def opponent(computer_card1,computer_card2, computer_hand):
  computer_card1 = randint(1,11)
  computer_card2 = randint(1,11)
  computer_hand = computer_card1 + computer_card2
  print(" ")
  print("COMPUTER: *randomized*")
  print("First Card Is: ",computer_card1)
  print("Second Card Is: ",computer_card2)
  print("Total: ",computer_hand)

  while computer_hand < 18: 
    computer_card = randint(1,11)
    computer_hand = computer_hand+computer_card
    print("Next card: ",computer_card)
    print("Total: ",computer_hand)
    if computer_hand > 21:
      print("computer busted")
      return
    if computer_hand == 21:
      print("computer hit 21!")
      return



