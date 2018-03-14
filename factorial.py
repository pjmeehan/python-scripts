# Patrick Meehan 13-03-2018
# exercise 6 - script for returning the factorial of a given number



def factorial(n): #n is my input of the function
    answer = 1
    while n >= 1: #as long as n is greater or equal to 1, the loop continues
        answer = answer * n  #answer is the place number while running thru the loop. it changes to a new varaible every time
        n = n - 1 #this will decrease n until it equals 1, then the loop will stop
    return answer # this is the output of the function

n = int(input("Please enter an integer: ",))   #allows for the input of a positive integer
print(factorial(n)) #will return the factorial based on the above script that I created for factorial(n)

