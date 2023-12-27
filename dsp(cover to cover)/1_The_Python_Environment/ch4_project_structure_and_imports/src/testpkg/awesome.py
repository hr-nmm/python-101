def greet():
    print("Hello, World!")


# print("Awesome module was run.") ## CASE-1

## CASE-2 __name__ is set to main when it is run directly via "python -m module.py"

if __name__ == "__main__":
    print("Awesome module was run.")
