'''
Write a function make_dict_from_elems_in_index that returns a dictionary consisting of a single key-value pair formed as follows:

the key is the element at the given index from the list keys.
the value is the element at the given index from the list values .
Assume the index is always within valid bounds for both lists.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

>>> keys = ['apple', 'banana', 'cherry']
>>> values = [10, 20, 30, 40]
>>> make_dict_from_elems_in_index(keys, values, 1) 
{'banana': 20}
>>> make_dict_from_elems_in_index(keys, values, -1) 
{'cherry': 40}

'''


keys = ['apple', 'banana', 'cherry']
values = [10, 20, 30, 40]


def make_dict_from_elems_in_index(keys, values, index):
    return {keys[index]: values[index]}

print(make_dict_from_elems_in_index(keys, values, 1))
print(make_dict_from_elems_in_index(keys, values, -1))


key1 = ["Arvind kumar", "Arru Sweetiee", "miss mdm"]
value1 = [10, 20, 30, 40]

def make_dict_form_elems_in_index(Key1, value1, index):
    return {key1[index]: value1[index]}

print(make_dict_form_elems_in_index(key1, value1, 1))
print(make_dict_form_elems_in_index(key1, value1,-1))
