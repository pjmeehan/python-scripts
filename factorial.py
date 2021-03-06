# Patrick Meehan 13-03-2018
# exercise 6, script for returning the factorial of a given number
# https://stackoverflow.com/questions/35467303/write-factorial-with-while-loop-python 

# Exercise 6
# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive
# integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers
# less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. You should, in your script,
# test the function by calling it with the values 5, 7, and 10.


# factorial definition (as per google dictionary) : the product of an integer and all the integers below it.


# n is my input of the function.
# the def function lets us name a function where we can use later just by using the named function rather than
# inputting the whole script again.

def factorial(n): 
    answer = 1

# create a loop with a 'while' statement to run through the given integer and all the integers below it.
# as long as n is greater or equal to 1, the loop will continue run.

    while n >= 1: 

# answer is the place number while running thru the loop. it changes to a new varaible every time.

        answer = answer * n  

# this will decrease n until it equals 1, then the loop will stop.

        n = n - 1 

# this is the output of the function.

    return answer

# use input statement to allow for the input of a positive integer

n = int(input("Please enter an integer: ",)) 

# use a print statement to return the factorial based on the above script that was created for factorial(n)


print(factorial(n)) 
