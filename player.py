from random import randint
import random

def game(card1,card2,hand,choices):

  card1 = randint(1,11)
  card2 = randint(1,11)
  
  hand= card1 + card2
  print(" ")
  print("PLAYER:")
  print("First Card Is: ",card1)
  print("Second Card Is: ",card2)
  print("Total: ",hand)
  while hand < 21:
    player=input("hit or stand? ")
    if player=="stand":
      print("your score is ", hand)
      return
    if player=="hit":
      card=randint(1,11)
      hand=hand+card
      print("Next card: ",card)
      print("Total: ",hand)
    if hand >21:
      print("you lose")
    if hand == 21:
      print("you win")
      
    