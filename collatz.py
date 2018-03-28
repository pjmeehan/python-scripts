# Patrick Meehan, 2018-02-08
# testing github repository update
# Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)

# basic premise : start with any positive integer n. Then each term is obtained from the previous term as follows:
# if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times
# the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

# set up script to allow user to input a number

x = int(input("Please enter an integer: "))

while x > 1: 
    print (x)     
    if x % 2 == 0:
        x = (int(x/2))
    else:
        x = (int((x*3)+1))
else:
    print (int(x)) 
