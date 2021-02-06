"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393936"


# he randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
from random import randint
a = randint (1,100)
if a < 50:
    if a < 25:
        print("Soon life will become more interesting") 
    else: 
        print("A beautiful person will be coming into your life")
else:
    if a < 75:
        print("Your life will be happy and peaceful.")
    else:
        print("You will solve a problem.")
print("Now, go spread positive vibes!")
