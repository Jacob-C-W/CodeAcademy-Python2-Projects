# Store RPS variable on play.
# Prompt the user to select RPS.
# Compare.
# Win or Lose.
# Inform player.

from random import randint
from time import sleep

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "Win": "Yippi! I won.",
  "Lose": "Aw dangit! I lost.",
  "Tie": "Yawn, boring! I hate ties."
}

def decide_winner(user_choice,computer_choice):
  print "Who do you think will win?"
  print "You selected %s" % user_choice
  print "I selected %s" % computer_choice
  if user_choice == computer_choice:
    print message["Tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["Won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["Won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["Won"]
  else: 
    print message["Lost"]

def play_RPS():
  print "Let's play Rock Paper Scissors!"
  user_choice = raw_input("So what'll it be? Rock, Paper, or Scissors?")
#  if user_choice != "Rock" or "Paper" or "Scissors" or "rock" or "paper" or "scissors":
#    print "Hey you have to choose one!"
#    return
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()

