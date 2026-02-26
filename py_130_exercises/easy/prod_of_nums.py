"""
Calculate the product of all numbers in a list using the reduce function.
"""

from functools import reduce


list_of_numbers = [1, 2, 3, 4, 5]
products = reduce(lambda x, y: x * y, list_of_numbers)

print(products)