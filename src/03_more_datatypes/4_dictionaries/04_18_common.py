'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}


'''

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}
result = {}

dict1_keys = set(_dict1.keys())
dict2_keys = set(_dict2.keys())


total_keys = list(dict1_keys.union(dict2_keys))
total_keys.sort()

for key in total_keys:
    result.update({key: _dict1.get(key,0)+_dict2.get(key,0)})

print(result)

