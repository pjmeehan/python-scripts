# Patrick Meehan 2018-02-19
# adapted from https://stackoverflow.com/questions/44008489/dice-rolling-simulator-in-python
# this is actaully someone else's program (see adapted above),I'm using it to see why mine isn't working

import random
repeat = True
while repeat:
    print("You rolled",random.randint(1,6))
    print("Do you want to roll again? Y/N")
    repeat = "Y" in input()