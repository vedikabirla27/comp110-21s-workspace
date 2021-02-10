"""An exercise in remainders and boolean logic."""

__author__ = "730393936"

numb = int(input("Enter an integer number: "))
if numb % 2 == 0:
    print("TAR")
if numb % 7 == 0:
    print("HEELS")
if numb % 2 == 0 and numb % 7 == 0:
    print("TAR HEELS")
else:
    print("CAROLINA")



# Begin your solution here...
