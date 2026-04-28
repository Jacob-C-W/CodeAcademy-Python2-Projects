# Roll a pair of dice.
# Add the values of the roll.
# Ask the user to guess a number.
# Compare the user’s guess to the total value.
# Determine the winner (user or computer).

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Give me your best guess!"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum roll is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "That's not even possible, try again!"
  else:
    print "Rolling..."
    sleep(2)
    print "You rolled a %d" % first_roll
    sleep (2)
    print "and a %d" % second_roll
    sleep(2)
    total_roll = first_roll + second_roll
    print "for a total of %d!" % total_roll
    sleep(2)
    if guess == total_roll:
      print "You win!"
    else:
      print "You lose!"

print "Roll the Dice"
roll_dice(6)
