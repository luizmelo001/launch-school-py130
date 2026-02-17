"""
Question 1
Create a generator expression that generates the reciprocals of the numbers from 1 to 10. 
A reciprocal of a number n is 1 / n. Use a for loop to print each value.
"""

reciprocals = (1/n for n in range(1,11))

#for value in reciprocals:
#    print(value)


"""
Question 2
Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. 
Use a for loop to print each value.
"""

def reciprocal_generator(n):
    counter = 1
    while counter <= n:
        yield 1/counter
        counter += 1

reciprocals = reciprocal_generator(10)

#for value in reciprocals:
#    print(value)

"""
Question 3
Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple
"""

fruits = ["apple", "banana", "cherry"]

c_fruits = (fruit.title() for fruit in fruits)
#print(tuple(c_fruits))


"""
Question 4
Create a generator function that generates the capitalized version of every string in a list of strings. 
Use a single print invocation to print all the capitalized strings as a tuple.
"""

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capitalize(strings):
    for string in strings:
        yield string.capitalize()

#print(tuple(capitalize(strings)))


"""
Question 5
Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. 
Use a single print invocation to print all the capitalized strings as a set.
"""

programming_languages = ["python", "java", "c++", "javaScript", "ruby"]

capitalized = (string.capitalize() 
               for string in strings 
               if len(string) >= 5)

#print(set(capitalized))


"""
Question 6
Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. 
Use a single print invocation to print all the capitalized strings as a set.
"""

def capitalize_short(strings):
    for string in strings:
        if len(string) < 5:
            yield string.capitalize()

print(set(capitalize_short(programming_languages)))
