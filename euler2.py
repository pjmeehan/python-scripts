# Patrick Meehan 2018-02-16

# project euler prob 2



fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n <= 40:
    i, j = j, i + j
    
  
  return i