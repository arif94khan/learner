try:
   print("Enter a numerator:")
   numer = int (input())
   print("Enter denominator:")
   denom = int (input())
   qoutient = numer / denom
   print(qoutient)
except ZeroDivisionError:
      print("Cannot divisble by zero")
      print("Enter denominator:")
      denom = int (input())
      qoutient = numer / denom
      print(qoutient)
