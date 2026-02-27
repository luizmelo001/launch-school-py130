"""
Use nested generator expressions to create a flat list of numbers from a list of lists.
"""

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def flatten(lst):
    gen = (item for nested in lst for item in nested)
    return list(gen)
