'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''


input = "hello world"
result_list=[]

a = input.split()
print(a)

for i in a:
    result_list.append(tuple(list(i)))

print(result_list)