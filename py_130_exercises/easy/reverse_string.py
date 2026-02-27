"""
Use a generator expression to yield each character of a string in reverse order.
"""

string = "Hello, World!"
gen = (char for char in reversed(string))

for char in gen:
    print(char)