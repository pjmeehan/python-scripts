# Patrick Meehan 2018-02-19
# exercise 4, euler problem 5

x = (11,13,16,17,19,20)

s = 2520

for i in range(len(x)):
  if s % x[i] == 0:
    print (s)
s = s + 1  
  
  
