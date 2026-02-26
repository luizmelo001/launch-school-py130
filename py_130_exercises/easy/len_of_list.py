"""
Use map to create a list of lengths of each string in the original list.
"""
def length_of_string(s):
    return len(s)

list_of_strings = ["apple", "banana", "cherry"]
lengths = list(map(length_of_string, list_of_strings))
print(lengths)

comp_len = [len(s) for s in list_of_strings]
print(comp_len)