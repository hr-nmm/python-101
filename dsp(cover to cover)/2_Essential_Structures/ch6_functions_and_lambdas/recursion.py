# factorial


def factorial(num: int) -> int:
    # n! = n* (n-1)!
    if num == 0:
        return 1
    return num * factorial(num - 1)


print(factorial(5))  # 120


## nth fibonacci number
def fibo(n: int) -> int:
    if n <= 1:
        return n
    return fibo(n - 2) + fibo(n - 1)


num = 7
for i in range(num):
    print(fibo(i), end=" ")  # 0 1 1 2 3 5 8
lst = [1.23, 4.56, 7.89]


## names store function reference when assigned
store = fibo
print(store, type(store))  # <function fibo at 0x7f3263df6440> <class 'function'>
