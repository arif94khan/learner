def add(a, b):
   return a + b

def sub(a, b):
   return a - b

def mul(a, b):
   return a * b

def div(a, b):
   return a / b
print("enter a value:")
a = float (raw_input())
print("enter b value:")
b = float (raw_input())
result = add(a,b), sub(a,b), mul(a,b), div(a,b)
print(a, b, result)
