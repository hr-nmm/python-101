def fibo_next(series: list[int] = [1, 1]) -> list[int]:
    series.append(series[-1] + series[-2])
    return series


fib1 = fibo_next()
print(fib1)  # prints [1, 1, 2]
fib1 = fibo_next(fib1)
print(fib1)  # prints [1, 1, 2, 3]

fib2 = fibo_next()
print(fib2)  # should be [1, 1, 2] but prints [1,1,2,3,5]
print(fibo_next())  # [1,1,2,3,5,8]


## appending happens no of times func runs
# never use mutable values for default argument values. Instead, use None as a default value, as shown in the following:
def fibonacci_next(series: list[int] = None) -> list[int]:
    if series is None:
        series = [1, 1]
    series.append(series[-1] + series[-2])
    return series


fib1 = fibonacci_next()
print(fib1)  # prints [1, 1, 2]
fib1 = fibonacci_next(fib1)
print(fib1)  # prints [1, 1, 2, 3]

fib2 = fibonacci_next()
print(fib2)  # should be [1, 1, 2] and prints [1, 1, 2]
print(fibonacci_next())  # [1,1,2]
