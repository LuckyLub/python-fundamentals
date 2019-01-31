'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

string=input("Give me some text, and i'll tel you how many vowels are in there.")
vowels=['a','e','u','i','o']

def count_letters(string, letters):

    string=list(string)

    for i in letters:
        count = 0
        for j in string:
            if i ==j:
                count += 1
        print(f"You used {count} times the vowel {i}")

count_letters(string,vowels)

#i may have been a little to enthousiastic up here.