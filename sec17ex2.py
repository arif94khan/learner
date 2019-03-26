import os

print("Enter file name to open:")
name = raw_input()
while not os.path.isfile(name):
    print("File does not exist.")
    print("Enter file name to open:")
    name = raw_input()
file = open(name, 'r')
for line in file:
    print(line)
