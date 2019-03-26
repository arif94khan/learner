def square(number):
   return number * number

numbers = [1,2,3,4,5]
print(numbers)
numberssq = list(map(square, numbers))
print(numberssq)
