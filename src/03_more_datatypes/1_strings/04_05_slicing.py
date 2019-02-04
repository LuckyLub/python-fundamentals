'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name=input('Who do you think you are? Give me your name, you swine!')

def pig_latin_compiler(name):
    return name[1:]+name[0]+'ay'

swine=pig_latin_compiler(name).capitalize()

print(f'I\'ll shall call you {swine}! Muahahaha!')