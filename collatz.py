# Patrick Meehan, 2018-02-08
# testing github repository update
# Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)

# basic premise : start with any positive integer n. Then each term is obtained from the previous term as follows:
# if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times
# the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

# set up script to allow user to input a number

x = int(input("Please enter an integer: "))

# run a while loop where x > 1 so that the script will only run if a positive integer is input.

while x > 1: 

# the print (x) statement will ask the user to input their number and will print that number.

    print (x)     

# using an if/else statement. start with a modulo to test if integer is even. if it is,
# it loops until an odd integer is found and defers top the else statment and runs that calculation for an odd integer.
# the loop will continue until it reaches 1.

    if x % 2 == 0:
                x = (int(x/2))
    else:
        x = (int((x*3)+1))

# using an else statement with the while statement. if the integer is not positive or x < 1, the else statement
# simply tells the script to just print what ever number was input. ie -8 will just print -8. 

else:
    print (int(x)) 
