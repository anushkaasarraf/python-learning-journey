# This program implements a simple Stone-Paper-Scissors game.
# The user plays against the computer, and the winner is decided using conditional logic based on the game rules.


import random
Computer = random.randint(1,3)
user = int(input("Enter 0 for Stone, 1 for Paper and 2 for scissors:"))
def winner(Computer, user):
  if((Computer == 0 and user == 1) or (Computer == 1 and user == 2) or (Computer == 2 and user == 0)):
    print("User wins")
  elif((Computer == 1 and user == 0) or (Computer == 2 and user == 1) or (Computer == 0 and user == 2)):
    print("Computer wins")
  elif(Computer == user):
    print("It's a tie")
  else:
    print("There must be an error")
winner(Computer,user)
