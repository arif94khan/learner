def even(number):
     if number % 2 == 0:
        return True
     else:
        return False
numbers = list(range(1,11))
print(numbers)
evens = list(filter(even, numbers))
print(evens)
