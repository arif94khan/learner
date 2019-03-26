def sum(x, y):
  return x + y
import functools
numbers = list(range(1,11))
print(numbers)
sum = functools.reduce(sum, numbers)
print("The sum is of the range is:" +str (sum))
