#!/usr/bin/env python3.10

## walrus operator -  assign a value to a variable and use that variable in another expression at the same time.

if (eggs := 7 + 5) == 12: print("We have one dozen eggs")
print(eggs)  # prints 12
#  assignment expression is that eggs is now a valid variable in the outer scope, so I can print its value outside of the conditional. This feature is potentially useful in many scenarios(conditionals loops,etc.)

## STRININGS
quote = "Shout \"Lebron, James!\""
# It is possible to avoid backslashes in this scenario, however:
quote = 'Shout, "Lebron, James!"'

# raw strings- here backlash is always treated as literal char. They’re preceded with an r,
print(r'I love forward and backlashes: \ \\ are\nt they cool')

# formatted strings - A third kind of string literal is a formatted string or f-string,
in_stock = 0
print(f"This cheese shop has {in_stock} types of cheese.")
## f-strings not limited to variables, can accept any python expression. It can be useful to print  both expression and its result using trailing'=' sign
print(f'{5+6=}') # # prints "5+6=11"

#CONcatenation

greeting = "Hello"
name = "Martin Shkreli"
# So far, you’ve seen concatenation with the addition (+) operator, like this:
message = greeting + ", " + name + "!"  # value is "Hello, Jason!"
print(message)
# Alternatively, I can use the join() method:
message = "".join((greeting, ", ", name, "!"))  # value is "Hello, Jason!"
print(message)

