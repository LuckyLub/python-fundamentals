'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = []
temp_list = []

for items, numbers in input_dict.items():
    temp_list.append(numbers)

temp_list.sort()

for i in temp_list:
    for items, numbers in input_dict.items():
        if numbers == i:
            result=[]
            result.append(items)
            result.append(numbers)
            result = tuple(result)
            result_list.append(result)

print(result_list)