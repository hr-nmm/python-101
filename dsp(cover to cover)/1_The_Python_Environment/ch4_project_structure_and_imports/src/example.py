from testpkg import awesome

awesome.greet()

# CASE-1(when a module or package is run directly, its __name__ is set to the value "__main__"): "Awesome module was run." ran first and then "Hello, World!" ran.

# CASE-2(when we did if __name__ == "__main__") then only func call ran because


print(__name__)  # __main__
print(awesome.__name__)  # testpkg.awesome
