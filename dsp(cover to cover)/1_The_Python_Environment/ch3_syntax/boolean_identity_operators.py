#!/usr/bin/env python3.10
spam,eggs,potatoes = True,False,None # python has dedicated none type equivalent to null value

if spam is True: print("We have Spam!") ## evaluates to True
if spam is not False: print("I dont like spam") ## evaluates to True
if spam: print("Spam, Spam, Spam ...") ## evaluates to True(PREFFERED)

if eggs is False: print("We're all out of eggs.") # Evaluates to True
if eggs is not True: print("No eggs, but we have spam, spam, spam, spam...") # Evaluates to True
if not eggs: print("Would you like spam instead?")# Implicitly evaluates to True (PREFFERED)

if potatoes is not None: print("Yum")  # Evaluates to False (preferred)  ## We never reach this...potatoes is None!
if potatoes is None: print("Yes, we have no potatoes.")# Evaluates to True (PREFFERED)

if eggs is spam: print("This won't work.")# Evaluates to False (CAUTION!!!- It  actually compares the identity of the variables, rather than the value. This is particularly troublesome, as the logic looks sound but is a bug waiting for a place to happen.)

## RULE:  use is only for comparing directly to None, and use regular comparison operators for everything else.


# TRUTHINESS: Most expressions and values in Python can be evaluated to a True or False value. This is typically done by using the value as an expression by itself, although you can also pass it to the bool() function to convert it explicitly

answer = 42
if answer:
    print("Evaluated to True")  # this run
print(bool(answer))             # prints True

## 0(int,float,string),False,None,empty sequences/iterables{Empty strings (''), lists ([]), tuples (()), sets (set()), and dictionaries ({}).} are Falsy in python, rest all are true.
