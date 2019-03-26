#Demonstrating arithmatic operations by using functions
#Declaring addition function passing a and b arguments
def add(a, b):
 return a+b

#Declaring substraction function passing a and b arguments
def sub(a, b):
  return a-b

#Declaring multiplication function passing a and b arguments
def mul(a, b):
 return a*b

#Declaring division function and passing a and b arguments
def div(a, b):
 return a/b


#main code
print("Enter arithmatic operation you want to perform(choose any one operation addition = +, subtraction= -, multiplication = *,division = /)")
op = raw_input()
#Reading a value
print("Enter a value:")
a = float (raw_input())
#Reading b value
print("Enter b value:")
b = float (raw_input())
#After reading the input from user checking and printing appropriate operation using if ..elif..
if op == '+':
#Calling addition funtion
   result = add(a,b)
   print("Addition of the given values is:" + str(result))
elif op == '-':
#Calling Subtraction function
   result = sub(a,b)
   print("subtraction of the given values is:"+ str(result))
elif op == '*':
#Calling Multiplication function
  result = mul(a,b)
  print("Multiplication of the given numbers is:" + str(result))
elif op == '/':
#Calling Division funtion
  result = div(a,b)
  print("Division of the given numbers is:" + str(result))
else:
   print("please choose one of the operation  +, -, *, /")
