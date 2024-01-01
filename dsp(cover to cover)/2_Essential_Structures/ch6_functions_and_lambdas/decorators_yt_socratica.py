import time
import functools, random

lst = [1, 3, 5, 2, -2, -4, 2]


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        dt = time.time() - begin
        print(f"delta t = {dt}")
        return result

    return wrapper


@timer
def sort_rev(lst):
    """wtf
    bro
    """
    return sorted(lst, reverse=True)


print(sort_rev(lst))
print(sort_rev.__doc__)
print(sort_rev.__name__)


#
def power():
    def f(x):
        return x**2

    def g(x):
        return x**3

    def h(x):
        return x**4

    functions = [f, g, h]
    to_be_executed = random.choice(functions)
    return to_be_executed


m = power()
am = m(3)
print(am)


## prime factorization
@timer
def prime_factors(num):
    lst = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            lst.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return lst


print(prime_factors(48))
