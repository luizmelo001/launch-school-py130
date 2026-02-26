"""
Remove all None values from a list using the filter method.
"""

list_with_none = [1, None, 2, None, 3, None, 4]
filtered_list = filter(lambda x: x is not None, list_with_none)