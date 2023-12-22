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

#-1.10 Sets - unodered collection of unique objects + no indexing + mutable
## use case: set(iterable) => returns a set with unique values
names1 = { 'IBM', 'MSFT', 'AA' }
names2 = set(['IBM', 'MSFT', 'HPE', 'IBM', 'CAT','IBM' ])
print(names1,names2) # {'MSFT', 'AA', 'IBM'} {'MSFT', 'HPE', 'IBM', 'CAT'}

## The elements of a set are restricted to immutable objects i.e, you can make a set of numbers, strings, and tuples only.
# set([[1,2,3],[1,2]]) # TypeError: unhashable type: 'list'

## set comprehension
names = {s[0] for s in portfolio[1:]}
print(names) ## { 'tata coffee', 'google'}

## set operations - union, intersection, difference, and symmetric difference
a = names1 | names2      # Union {'MSFT', 'CAT', 'HPE', 'AA', 'IBM'}
print(a)
b = names1 & names2      # Intersection {'IBM', 'MSFT'}
print(b)
c = names1 - names2      # Difference { 'AA' }
print(c)
d = names2 - names1      # Difference { 'CAT', 'HPE' }
print(d)
e = names1 ^ names2      # Symmetric difference(a U b - a intesecn b) { 'CAT', 'HPE', 'AA' }
print(e)

## New items can be added to a set using add() or update():
names2.add('TTL') ## add a single item
print(names2) # {'CAT', 'IBM', 'HPE', 'TTL', 'MSFT'}
names1.update({'JJ', 'GE', 'ACME'}) ## add multiple items
print(names1) # {'AA', 'IBM', 'GE', 'ACME', 'MSFT', 'JJ'}

## An item can be removed using remove() or discard():
names2.remove('IBM') # Remove 'IBM' or raise KeyError if absent.
names1.discard("GGL") # Remove 'GGL' if it exists.

#-1.11 Dictionaries
 ## A dictionary is a mapping between keys and values. 
s = { 'name' : 'GOOG', 'shares' : 100, 'price' : 490.10 }
## accessing like indexing  with keys
print(s['name'],s['price']) #  GOOG 490.1

## Inserting or modifying objects works like this:
s['shares'] = 75 ## modifying 100 shares with 75
s['date'] = '2007-06-07' ## inserting a new 'date' key with value "2007-06-07"
print(s) # {'name': 'GOOG', 'shares': 75, 'price': 490.1, 'date': '2007-06-07'}

## Dictionary membership is tested with the in operator:
prices ={ 'GOOG' : 490.1,'AAPL' : 123.5, 'IBM' : 91.5,'MSFT' : 52.13 }
p_variable = prices['IBM'] if 'IBM' in prices else 0.0
print(p_variable) # 91.5
##  same thing can be written using get function: dict.get("key",val)
p_variable = prices.get("TTL",32.0)  
print(p_variable) # 32.0

## Use the del statement to remove an element of a dictionary:
del prices['GOOG']
print(prices)

## 1. TABULATION PROBLEM - count the total number of shares for each stock name
portfolio = [
   ('ACME', 50, 92.34),
   ('IBM', 75, 102.25),
   ('PHP', 40, 74.50),
   ('IBM', 50, 124.75)
]
### { s[0]: 0 for s in portfolio } is an example of a dictionary comprehension making an initial dictionary mapping stock names to 0.
total_shares = {tple[0]:0 for tple in portfolio}
print(total_shares) # {'ACME': 0, 'IBM': 0, 'PHP': 0}
for name,shares,_ in portfolio:
    total_shares[name] += shares
print(total_shares) # {'ACME': 50, 'IBM': 125, 'PHP': 40}

### collections module has a Counter object that can be used for this task:
from collections import Counter
total_shares1 = Counter()
for name,shares,_ in portfolio:
    total_shares1[name] += shares
print(total_shares1) # Counter({'IBM': 125, 'ACME': 50, 'PHP': 40}) => this has type counter
total_shares1 = dict(total_shares1)
print(total_shares1) # {'ACME': 50, 'IBM': 125, 'PHP': 40}

## key-val pairs in a list can be directly converted to dict using dict():
pairs = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
d = dict(pairs)
print(d) # {'IBM': 125, 'ACME': 50, 'PHP': 40}

## dict.keys()
d = { 'x': 2, 'y':3 }
k = d.keys()
print(k) # dict_keys(['x', 'y'])
d['z'] = 4
print(k) ## k is a dict_keys object which is mutable on every dictionary update.

## use of dict.items() : used to loop over a dictionaries
for key,value in d.items(): ## if we fo for key,val in d:  => gives error
    print(f'key:{key}=value:{value}',end = " ") # key:x=value:2 key:y=value:3 key:z=value:4


#-1.12 Iteration and Looping
## uses of range():1- in for loop, 2- in operator  with range
for i in range(8, 1, -1) :
   print(i,end= " ") # 8 7 6 5 4 3 2 
print(7 in range(1,10)) # True
print(4.5 in range(1,10)) # False


#-1.13 Functions
##  Use the def statement to define a function divide which returns a tuple quotient,remainder:
def divide(a: int,b: int) -> (int,int): ## a,b are 2 integers
    return a//b,a-(a//b)*b
q,r = divide(14,3) # When multiple values are returned in a tuple, they can be unpacked into separate variables like this:
print(q,r) # 4 2

## To assign a default value to a function parameter, use assignment:
## def connect(hostname, port, timeout=300):
##       -- Function body -- ()

## connect('www.python.org', 80)                 => calling style 1
## connect(port=80, hostname='www.python.org')   => calling style 2
## connect('www.python.org', 80, 500)            => calling style 1   
## connect('www.python.org', 80, timeout=500)    => calling style 2


#-1.14 Exceptions
## 
#
import os
print(os.__file__)



















#-1.15 Program Termination
#-1.16 Objects and Classes
#-1.17 Modules
#-1.18 Script Writing
#-1.19 Packages
#-1.20 Structuring an Application
#-1.21 Managing Third-Party Packages
#-1.22 Python: It Fits Your Brain