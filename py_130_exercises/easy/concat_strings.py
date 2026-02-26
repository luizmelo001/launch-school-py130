from functools import reduce

"""
Use reduce to concatenate a list of strings into a single string.
"""

list_of_strings = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, list_of_strings)
print(concatenated_string)  # Output: "Hello World!"