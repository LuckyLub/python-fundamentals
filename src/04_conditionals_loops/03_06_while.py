'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
i=1

while i <= 1000:
    if i % 5 == 0:
        print(i)
    i += 1