try:
   print("Enter the name of a file:")
   name = raw_input()
   file = open(name, 'r')
except IOError:
               print("Cannot open file:")
               print("Enter the name of the file to open:")
               name = raw_input()
               file = open(name, 'r')
