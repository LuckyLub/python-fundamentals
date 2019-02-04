'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list=[]

#this code below didn't work, but i don't understand why...
'''def mySorter(x):
    print(x[1])
    return x[1]

sorted_list=unsorted_list.sort(key=mySorter)'''


sorter1=[]
sorter2=[]

for j in unsorted_list:
    sorter1.append(j[1])
    sorter2.append(j[1])

sorter2.sort()

for j in sorter1:
    sorted_list.append(unsorted_list[sorter2.index(j)])

print(sorted_list)

