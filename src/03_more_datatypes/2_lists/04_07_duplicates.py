'''

Write a script that removes all duplicates from a list.

'''

list_a=[0,1,2,3,4,4,4,4,4,4,4,4]

def duplicate_removal(list_a):
    list_a=list(set(list_a))
    return list_a

print(duplicate_removal(list_a))