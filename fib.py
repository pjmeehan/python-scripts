# Ian McLoughlin
# Exercise 1, a program that displays Fibonacci numbers.

# Exercise : Please complete the following exercise this week. In the video lectures this week we ran an example
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