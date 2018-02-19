# Patrick Meehan
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import random
roll_again = True

while roll_again:
    print ("you rolled a ...", random.randint(1,6))
    print ("would you like to try again?")
    roll_again == "y", input()
else:
    roll_again == "n"
    print ("thanks for playing")    