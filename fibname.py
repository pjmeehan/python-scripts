# # Patrick Meehan March 28, 2018
# Exercise 1, a program that displays Fibonacci numbers.
# Exercise 2, a program that displays Fibonacci numbers involving people's names.
# based on scripts created by Ian McLoughlin.

# Exercise 1
# Please complete the following exercise this week. In the video lectures this week we ran an example
# program that calculated the 30th Fibonacci number. Change the program to calculate the nth Fibonacci number
# where n the sum of the first and last letters of your first name as numbers. Take A as the number 1, B as 2,
# C as 3, and so on. For example, my name is Ian, so I should calculate the 25th Fibonacci number because I is 9
# and n is 14, giving 25 in total.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 27
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Answer submitted to discusions
# My name is Patrick, so the first and last letter of my name (P + K = 16 + 11) give the number  27. The 27th Fibonacci number is 196,418.




 
# A program that displays Fibonacci numbers using people's names.
# based on a script created by Ian McLoughlin, see link on next line
# https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py

# Exercise 2
# Copy and run the program yourself. Change the string variable to contain your own surname, and rerun it.
# Can you figure out what ord() does? Try to Google it to find out
 
 def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Meehan"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Answer submitted to discusions
# My surname is Meehan

# The first letter M is number 77

# The last letter n is number 110

# Fibonacci number 187 is 538522340430300790495419781092981030533

# ord() returns an integer representing the code of the character.
