import os
files = os.popen('dir *.py')
fileit = iter(files)
for file in files:
    print(file)
