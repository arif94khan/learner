sentence="Service to humanity is service the God"
count=0
for letter in sentence:
     if letter == 'a' or letter == 'e' or letter == 'i' or letter =='o' \
      or letter == 'u':
      count= count +1
print("The number of vowels is:" +str(count))
