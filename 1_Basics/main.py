#-1.1 Running Python - use an interpreter(by writing python in the termianal) which is a REPL(read-evaluation-print loop) => it executes statements then and there.

#-1.2 Python Programs - use .py extension(to reuse scripts) to save code and editor like VScode(for productivity)
print("Hello World!")

#-1.3 Primitives-(int,float,string,bool), Variables, and Expressions
## - A variable is a name that refers to a value. A value represents an object of some type:
x = 42
## - An expression is a combination of primitives, names, and operators that produces a value.
exp = (x +3) //5
print(exp) # 9

## compound interest 
principal = 1000        # Initial amount
rate = 0.05             # Interest rate
numyears = 5            # Number of years
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print(f'{year:>3d} {principal:0.2f}')
    year += 1 ## o/p: 1 1050.00   2 1102.50   3 1157.62   4 1215.51    5 1276.28
    ## '>3d' means a three-digit decimal number, right aligned. '0.2f' means a floating-point number with two decimal places of accuracy.


#-1.4 Arithmetic Operators(+,-,*,/,//(truncating division),**(power),%(modulo))
    ## Comparison Operators (<,>,<=,>=,==,!=) => The result of a comparison is a Boolean value True or False.
    ## Logical Operators also return Bool (or,and,not)
print(not(3>2)) # False
    ## Common math functions(abs,pow,round,divmod(Return the tuple (x//y, x%y)))
print(divmod(5,2)) # (2,1)

#-1.5 Conditionals(if,else,elif) and Control Flow(while statements) 
## break vs continue 
x = 0
while x < 10:
    if x == 5:
        break # Stops the loop. Moves to Done below
    print(x)
    x += 1
print('Done') #0,1,2,3,4,'Done' are printed
  ## The continue statement skips the rest of the loop body and goes back to the top of the loop.
x = 0
while x < 10:
    x += 1
    if x == 5:
       continue   # Skips the print(x). Goes back to loop start.
    print(x)

print('Done')  #1,2,3,4,6,7,8,9,10,'Done' are printed 5 is skipped

## min(),max()
print(max(1,2,3),min(1,2,3)) # 3 1
## NOTE: In Python, inbuilt funcs max(a, b) is generally more efficient than maxval = a if a > b else b, because max(a,b) is written in C.

#-1.6 Text Strings
## Strings are stored as sequences of Unicode characters indexed by integers, starting at zero.
string = "Hello World"
print(len(string)) # 11
print(string[4],string[-1],string[:5],string[6:],string[3:8]) # 'o'  'd'  'Hello'  'World'  lo Wo'

## Strings are concatenated with the plus (+) operator
print(string+'ly') # Hello Worldly

## repr() creates a string that you type into a program to exactly represent the value of an object.
## repr() to be used while debugging
s = 'hello\tworld'
print(str(s)) # hello   world
print(repr(s)) # hello\tworld

## The format() function is used to convert a single value to a string with a specific formatting applied.BELOW BOTH ARE SAME:
num = 12.34567
print(format(num,'0.2f')) # 12.35
print(f'{num:0.2f}') # 12.35


#-1.7 File Input and Output
##  [with open as] is used to avoid forgetting of file.close() vs open(file)  close(file)
file = open('doc.txt')
print(list(file)) ## ['This is a simple text file.\n', 'This is the second(2nd) line of the file.\n', 'This is the third(3rd) line of the file.']
## open() func returns a new file object which is iterable.
for line in file:
    print(line,end=' ') ## prints each line of the doc.txt file
file.close()

## If you want to read the file in its entirety as a string, use the read() method like this:
with open('doc.txt') as file:
    data = file.read()
    print(type(data),data) ## <class 'str'>   [whole string of doc.txt file]

## to read data typed interactively in the console use input()
# name = input('Enter your name : ')
# print('Hello', name)

## to write something(like o/p of a program) to a file use:  file_obj.write(string)
with open('doc.txt',"a") as file_obj:
    file_obj.write(f'\n{year:>3d} {principal:0.2f}')

## 'a' is append mode, 'w' is write mode(overwrites existing string), default is read mode


#-1.8 Lists (ordered collection) - mutable
## indexing, assigning new item to list,append,insert,loop
names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]
print(names[2]) # Thomas
names[2] = 'Tom'
print(names) # ['Dave', 'Paula', 'Tom', 'Lewis']
names.append("Kobe")
names.insert(2,"Lebron") ## "Tom" will shift one place to right
print(names) # ['Dave', 'Paula', 'Lebron', 'Tom', 'Lewis', 'Kobe']
for name in names:
    print(name,end=' ') # Dave Paula Lebron Tom Lewis Kobe

## "+' operator to conacatenate lists
print([1,2,3]+['s','p']) # [1, 2, 3, 's', 'p']
#-1.9 Tuples are ordered immutable
portfolio = list() ## list of tuples
with open("portfolio.csv") as file:
    for line in file:
        row = line.split(",")
        name = row[0]
        share = row[1]
        price = row[2].rstrip('\n')
        holdings = (name,share,price)
        portfolio.append(holdings)
print(portfolio) ##[('name', 'share', 'price'), ('google', '20', '350'), ('tata coffee', '14', '25')]
print(type(portfolio[1]),portfolio[1]) # <class 'tuple'> ('google', '20', '350')

## to calculate total value of the portfolio
total = sum([int(shares) * int(price) for _, shares, price in portfolio[1:]])
print(total) # 7350 (which is 20*350+14*25)
## learnt unpacking og tuples/variables in loop and use of '_'

#-1.10 Sets
#-1.11 Dictionaries
#-1.12 Iteration and Looping
#-1.13 Functions
#-1.14 Exceptions
#-1.15 Program Termination
#-1.16 Objects and Classes
#-1.17 Modules
#-1.18 Script Writing
#-1.19 Packages
#-1.20 Structuring an Application
#-1.21 Managing Third-Party Packages
#-1.22 Python: It Fits Your Brain