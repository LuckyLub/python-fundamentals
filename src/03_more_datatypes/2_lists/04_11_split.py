'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

userString=input("Please, type a sentence without using syntax.")
userStringSplitted = userString.split()

count=0

for word in userStringSplitted:
    if userStringSplitted.count(word)>count:
        count=userStringSplitted.count(word)
        max=word

print(f'The word you pronounced most often is: {max}.')