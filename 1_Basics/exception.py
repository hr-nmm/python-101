# while True:
#     try:
#         x = int(input("what is x?"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# 
# print(f'x is {x}')

## below is the same program 
def main():
    x = get_x("what is x?")
    print(f"x is {x}")

def get_x(prompt):
    while True:
        try:
            return int(input(prompt)) ## we dont use else:break beacause return breaks the loop 
        except ValueError:
            print("x is not an integer. Please provide an int value.")

main()
