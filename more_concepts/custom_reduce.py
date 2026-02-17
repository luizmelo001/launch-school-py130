"""
Docstring for custom_reduce

The reduce function reduces the elements in an iterable object to a single value. 
For instance, reduce can return the sum of all numbers in a list or concatenate the strings in a tuple to form a single long string. 
It's a bit like map, but instead of returning a new collection, it just returns a single value.
"""

def reduce(callback, iterable, accum):
    result = accum

    for item in iterable:
        tmp = callback(item, result)
        result = tmp

    return result


numbers = [10, 3, 5]
product = lambda number, accum: accum * number
#rint(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
#print(reduce(total, numbers, 0))        # 31

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV


"""
Use the reduce function shown in the answer to the previous question to compute the sum of the squares in a list of numbers.
"""

nums = [3, 7, 2, 9, 5]
total = reduce(lambda number, accum: number**2 + accum, nums, 0)
print(total)        # 168

squares = lambda num, accum: num**2 + accum
print(reduce(squares, numbers, 0))