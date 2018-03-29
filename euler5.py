# Patrick Meehan 2018-02-19
# exercise 4, euler problem 5
# https://projecteuler.net/problem=5

# Exercise 4
# Please complete the following exercise this week. It is problem 5 from Project Euler. The problem is as follows. 
# 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
 
#original attempt
# s = 2520 # we know 1 thru 10 lowest number is 2520, so we start with that number and eliminate the need of going thru range 1 thru 10 again.

# for i in range(11, 21, 20):  ## we know 1 thru 10, so start range with 11 thru 21 in steps of 20 because we know the number we are looking for must be divided by 20
#  if s % x[i] == 0:
#    print (s)
# s = s + 1  

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 

# frustrated with many attempts, I used google for help and came across the following youtube video
# which I actually understood.
# https://www.youtube.com/watch?v=EMTcsNMFS_g

# created a function with a "for in range". 
def find(n):

# we know 2520 is the answer to 1 thru 10, so start range with 11 thru 21.

  for i in range(11, 21):  
    if n % i == 0:

# if the iteration is evenly divisable, the script will 'continue' to the next iteration     
      continue
# if the iteration is not evenly divisable, the script will 'return a false' and move to the next number n.      
    else:
      return False
# once the script finds a number that is evenly divisable by all iterations, it will 'return a true'.      
  return True

# next we write a script to run our function.
# we know that 2520 is the lowest number 1 thru 10. so we start with that number
# and eliminate the need of going thru range 1 thru 10 again.

x = 2520

# use a 'while true' to keep looping until our (x) in find (x) finds the lowest number that is divisable by 
# all the numbers 11 thru 20. Once found, the scripts stops with a 'break' statement.
while True:
  if find(x):
    break

# we increase the number by 2520 becuase we know that it is the smallest positive number
# evenly divisble by all the numbers from 1 to 10. since we are looking for the smallest positive
# number evenly divisable from 1 to 20, and we know 1 to 10 is 2520, the number we are looking for must be
# divisable by 2520. 
     
  x = x + 2520

print (x)
  
