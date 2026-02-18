"""
Create a list where each number from the original list is squared using the map method.
"""


lst = [1, 2, 3, 4]
squared_lst = list(map(lambda x: x**2, lst))
print(squared_lst)