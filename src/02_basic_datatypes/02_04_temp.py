'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

def F_to_C(F):
    return (F - 32) * (5 / 9)

F=float(input('What degrees is it outside in Fahrenheit?'))

print(round(F,2), ' degrees fahrenheit = ', round(F_to_C(F),1),' degrees celsius')