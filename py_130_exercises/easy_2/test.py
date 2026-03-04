from functools import partial

"""
Create three different partial versions using three different styles:

Using functools.partial
Using lambda
Using a def wrapper function

Then call each one like this:

print(hello("Luiz"))     # Hello, Luiz!
print(hi("Maria"))       # Hi, Maria!
print(hey("everyone"))   # Hey, everyone!

"""

def greet(greeting, name):
    return f"{greeting}, {name}!"

#lambda
hello = lambda name: greet("Hello", name)
print(hello("Luiz"))     # Hello, Luiz!

#partial
hi = partial(greet, "Hi")
print(hi("Maria"))

#wrapper
def hey(name):
    return greet("Hey", name)

print(hey("everyone"))


"""
You have this function:
def format_price(amount, currency="R$", decimals=2):
    return f"{currency} {amount:,.{decimals}f}"
Create a partial version called format_brl that:

always uses currency="R$"
always uses decimals=2

Then test it:
print(format_brl(1234.567))         # R$ 1,234.57
print(format_brl(99))               # R$ 99.00
print(format_brl(0.5, decimals=3))  # should still allow overriding decimals
"""

def format_price(amount, currency="R$", decimals=2):
    return f"{currency} {amount:,.{decimals}f}"

def format_brl(amount, decimals=2):
    return format_price(amount)

#format_brl = partial(format_price, currency="R$", decimals=2)

print(format_brl(0.5, decimals=3))  # should still allow overriding decimals


"""
# Convert all temperatures to Fahrenheit using the standard formula
f_temps = list(map(..., temperatures_c))
print(f_temps)  # [32.0, 50.0, 68.0, 86.0, 212.0]
Do it in two ways:

once with functools.partial
once with lambda
"""
temperatures_c = [0, 10, 20, 30, 100]

def convert_to_f(celsius, offset=32, factor=1.8):
    return celsius * factor + offset

# Using functools.partial
fahrenheit_partial = partial(convert_to_f, offset=32, factor=1.8)

# Using lambda
fahrenheit_lambda = lambda c: convert_to_f(c, offset=32, factor=1.8)

# Using wrapper function
def fahrenheit_wrapper(celsius):
    return convert_to_f(celsius, offset=32, factor=1.8)

f_temps_partial = list(map(fahrenheit_partial, temperatures_c))


"""
Given a function: python def power(base, exponent): return base ** exponent Create partials square and cube that fix the exponent.
int_base2("1010")   # 10
int_base16("FF")    # 255
"""


"""
add_element_pure(seq, value) that returns a new list with value appended, without modifying seq.
add_element_inplace(seq, value) that modifies seq directly and returns None.
"""

def add_element_pure(seq, value):
    # This is a PURE function
    # ────────────────────────────────────────────────────────
    # • It never modifies the input sequence (seq)
    # • It creates and returns a brand new list instead
    # • Same inputs → always produces the same output
    # • No side effects (no mutation, no printing, no file I/O, etc.)
    # ────────────────────────────────────────────────────────
    return seq + [value]    

def add_element_inplace(seq, value):
    # This is a PURE function
    # ────────────────────────────────────────────────────────
    # • It never modifies the input sequence (seq)
    # • It creates and returns a brand new list instead
    # • Same inputs → always produces the same output
    # • No side effects (no mutation, no printing, no file I/O, etc.)
    # ────────────────────────────────────────────────────────
    seq.append(value)   # ← append() returns None !!

my_list = [1, 2, 3]
new_list = add_element_pure(my_list, 4)
print(new_list)  # [1, 2, 3, 4]
print(my_list)   # [1, 2, 3]
