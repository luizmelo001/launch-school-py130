"""
Obtain only the even numbers from a list using the filter function.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x %2 == 0, lst)
