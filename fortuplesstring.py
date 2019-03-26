words = ("now","is","the","time")
for word in words:
    print(word)
max=0    
for i in range(1,len(words)):
    if  len(words[i]) > len(words[max]):
      max=i
print("The longest word is:"  + words[max])
