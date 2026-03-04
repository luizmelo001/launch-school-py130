numbers = [1, 2, 3, 4, 5, 6]

x, y, *remainder = numbers

print(x)          # Output: 1
print(y)          # Output: 2
print(remainder)  # Output: [3, 4, 5, 6]

numbers = [1, 2, 3]
a, *middle, c = numbers

print(a)        # Output: 1
print(middle)   # Output: [2]
print(c)        # Output: 3