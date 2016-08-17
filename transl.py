print ('Welcome to the Pig Latin Translator!')
py = 'ay'
original = input("Enter a word:")
word = original.lower()
first = word[0]
new_word = word+first+py
if len(original) > 0 and original.isalpha():
    print (original)
else:
    print ("empty")