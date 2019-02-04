'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

n = 10
i = 1
myDict={}

while i <= 10:
    myDict.update({i : i**2})
    i+=1

print(myDict)