import userdmodule

def square(number):
    print("not from userdmodule module")
    return number * number

num = 12
print("Square from userdmodule.py:")
print(userdmodule.square(num))
print("Square from main program:")
print(square(num))
