# VARIABLES(in python) : NAMES + VALUES
spam = 123_456_789
maps = spam
eggs = 123456789

print(spam == maps)
print(spam == eggs)

print(spam is maps)
print(spam is eggs)
print(
    id(spam), id(maps), id(eggs)
)  ## id() is similar to is : id(x) == id(y) equvalent to x is y; both check memory address of reference

a = 3
b = a
a = 4
print(a, b)  # 4 3


# In python, everything is an object, in fact class is also an object.
class A:
    pass


print(type(A), type(2), type("this is a string"))
# <class 'type'> <class 'int'> <class 'str'>

## usecase of type()
answer = 42
if type(answer) is int:
    print("Run this block")
##  "isinstance" is better practice
if isinstance(answer, int):
    print("Run this block")

# Duck Typing is a type system used in dynamic languages. For example, Python, Ruby, PHP, Javascript, etc. where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.


## Scope 4 pts - funcs define their own scope,classes/modules,scope-end names deleteion, python's reference counting garbage collection
def spam():
    message = "spam"
    word = "any"
    print("dunc spam() running,", message, word)  # func spam() running, spam any
    return message


output = spam()
print(output)  # spam => value is not deleted coz it was returned by func spam()

# here output is a global name but message is a local name restricted to the scope of func spam()
