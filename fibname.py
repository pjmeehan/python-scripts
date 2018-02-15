# Ian McLoughlin
# A program that displays Fibonacci numbers.
# Exercise 1

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




# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# Exercise 2

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
