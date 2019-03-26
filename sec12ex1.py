def countletters(words):
    if len(words) < 1:
        return 0
    else:
      return len(words[0]) + countletters(words[1:])

sentence = ['now', 'is', 'the', 'time']
print(sentence)
print(countletters(sentence))
