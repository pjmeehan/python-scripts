# Patrick Meehan 2018-02-19
# exercise 4, euler problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 

# created a function with a "for in range" to find 
def find(n):

# we know 1 thru 10, so start range with 11 thru 21 

  for i in range(11, 21):  
    if n % i == 0:
      continue
    else:
      return False
  return True

# we know that 2520 is the lowest number 1 thru 10. so we start with that number
# and eliminate the need of going thru range 1 thru 10 again.

x = 2520

while True:
  if find(x):
    break

# we increase the number by 2520 becuase we know that it is the smallest positive number
# evenly divisble by all the numbers from 1 to 10. since we are looking for the smallest positive
# number evenly divisable from 1 to 20, and we know 1 to 10 is 2520, the number we are looking for must be
# divisable by 2520.
     
  x = x + 2520

print (x)
  
