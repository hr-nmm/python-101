#
def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value} ")


# first == therefore
# mid == I
# last == am


# Driver code
myFun(first="therefore", mid="I", last="am")


## another example
def call_sth_else(func, *args, **kwargs):
    return func(*args, **kwargs)


def say_hi(name):
    print(f"Hello {name}")


call_sth_else(say_hi, name="bob")  # func passed as an object
## o/p: Hello bob
