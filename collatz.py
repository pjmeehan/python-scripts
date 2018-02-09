# Patrick Meehan, 2018-02-08
# Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)

x = int(input("Please enter an integer: "))

while x > 1: 
    print (x)     
    if x % 2 == 0:
        x = (int(x/2))
    else:
        x = (int((x*3)+1))
else:
    print (int(x)) 
