# Patrick Meehan 2018-02-22
# testing different list functions
# To pull information from CSV files you use loop and split methods to get the data from individual columns (http://www.pythonforbeginners.com/csv/using-the-csv-module-in-python)

# euler5.py

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

# This is translated from some C++ code I found regarding this problem.

check = 2520
# check is set to 2520 because we already know is is the smallest number
# that can be divided by each of the numbers # from 1 to 10 without any remainder.
# we can use this as our starting point

i = 11
# i is set to 11 because we already know the solution of 
# numbers between 1 to 10 (2520).

while (i != 20):
    i = i+1
    if (check % i != 0):
        check = check + 2520
        i = 1
print ("%d", %, check)