'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4

'''

def place_of_letter(string, letter):
    place = string.find(letter)
    return place

string = input("Give me a string, quickly.")
letter = input("Now a letter you just used!")

x = place_of_letter(string,letter)

while x ==-1:
    letter = input("You didn't use that letter in your string, pal! Give me another one!")
    x = place_of_letter(string,letter)

print(f"Cool. The first time this letter was mentioned, was on place {x+1}!")


