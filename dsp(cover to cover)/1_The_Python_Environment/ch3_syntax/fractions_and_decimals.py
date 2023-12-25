#!/usr/bin/env python3.10
from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)  # 1/3
print(third_fixed)     # 0.333
print(third_float)     # 0.3333333333333333

third_float = float(third_fraction)
print(third_float)     # 0.3333333333333333

third_float = float(third_fixed)
print(third_float)     # 0.333

## some math operators
print(-42)         # negative (unary), evaluates to -42
print(abs(-42))    # absolute value, evaluates to 42 , also unary, rest below are all binary
print(40 + 2)      # addition, evaluates to 42
print(44 - 2)      # subtraction, evaluates to 42
print(21 * 2)      # multiplication, evaluates to 42
print(680 / 16)    # division, evaluates to 42.5
print(680 // 16)   # floor division (discard remainder), evaluates to 42
print(1234 % 149)  # modulo, evaluates to 42
print(7 ** 2)      # exponent, evaluates to 49
print((9 + 5) * 3) # parentheses, evaluates to 42

# augumented assignment operations
foo = 10
foo += 10   # value is now 20 (10 + 10)
foo -= 5    # value is now 15 (20 – 5)
foo *= 16   # value is now 240 (15 * 16)
foo //= 5   # value is now 48 (240 // 5)
foo /= 4    # value is now 12.0 (48 / 4)
foo **= 2   # value is now 144.0 (12.0 ** 2)
foo %= 51   # value is now 42.0 (144.0 % 15)

## math module
import math

print(math.pi)   # PI
print(math.e)    # Euler's number
print(math.inf)  # Infinity
print(math.nan)  # Not-a-Number

infinity_1 = float('inf')
infinity_2 = math.inf
print(infinity_1 == infinity_2) # True