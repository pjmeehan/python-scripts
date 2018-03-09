# Patrick Meehan 2018-02-19
# exercise 4, euler problem 5

 

s = 2520 # we know 1 thru 10 lowest number is 2520, so we start with that number and eliminate the need of going thru range 1 thru 10 again.

for i in range(11, 21, 20):  ## we know 1 thru 10, so start range with 11 thru 21 in steps of 20 because we know the number we are looking for must be divided by 20
  if s % x[i] == 0:
    print (s)
s = s + 1  
  
  
