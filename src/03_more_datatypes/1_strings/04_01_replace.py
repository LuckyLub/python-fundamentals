'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

def weird_script(text, symbol):
    return text.replace(text[0],symbol)

t = input("Hi there! Type something for me!")
s = input("Now give me a symbol!")

print("Look at this:", weird_script(t,s))