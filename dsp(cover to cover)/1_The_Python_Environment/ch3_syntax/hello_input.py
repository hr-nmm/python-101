#!/usr/bin/env python3
name = input("What is your name?")
print("Hello " + name.capitalize()) # Hello Kobe

## to pack multiple statements in one line, separate them with a semi-colon(;)
message = "Hello, world!"; print(message) # Hello, world!

## 
raining,hailing = True,False
print( "nope" if hailing else "Umbrella time" if raining else "enjoy sun")
## why i cant do pass instead of "enjoy sun" beacuse the expression has to be evsaluated with a value