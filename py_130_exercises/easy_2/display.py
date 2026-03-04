"""
Write a function display_info that takes a positional-only parameter data, and keyword-only parameters reverse and uppercase.

"""

def display_info(data, /, *, reverse=False, uppercase=False):
    if reverse:
        data = data[::-1]
    if uppercase:
        data = data.upper()
    print(data) 