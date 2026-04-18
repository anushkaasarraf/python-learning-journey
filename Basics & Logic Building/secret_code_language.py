# This program converts a normal message into a secret code language.
# For words with length less than 3, the word is reversed.
# For longer words, the first letter is moved to the end and random characters are added at the beginning and end.


str = input("Enter a message:")
words = str.split(" ")
nwords = []
for word in words:
  word_characters = len(word)
  word_list = []
  random_list1 = ['p','t','a']
  random_list2 = ['j','k','r']
  for i in word:
    word_list.append(i)
  if word_characters < 3:
    word_list.reverse()
    nword = "".join(word_list)
  else:
    word_list.pop(0)
    word_list.append(word[0])
    new_list = random_list1 + word_list + random_list2
    nword = "".join(new_list)
  nwords.append(nword)
print(" ".join(nwords))
