"""
Lambda function

* anonymous function
* any number of arguments
* only 1 expression

"""
x = lambda a, b : a * b
print(x(5, 6)) 

x = lambda a: a * 3 + 3
print(x(1))

"""
Generators
* "lazy" on demand operation of values
    * lower memory consumption
* allow you to declare a function that behaves like an iterator
* used in a for loop to simplify code ane make more memory efficient
* can use next to call a genrator
* Ex to save memory
    * Adding list of numbers
    * what if 1 billion floating point numbers
    * for loop / range function builds a list in memory
    * But generators and xrange generate new list values every time access
        whereas range is static list reused
    * produces a sequence of results, maintains a local sttate, 
     so that fnction can resume where it left off 
    * function containeing "yield" is a gnerator 

    *  Returns sneds sepcified value back to caller (hYields)a
    * use yield when want to iterate over a large list and don't want to 
      contain the entire sequence in memory
 
"""
# use a for loop
numbers = list()

for i in range(100):
    print(i)
    numbers.append(i+1)

total = sum(numbers)
print('total numbers', total)

# use a generator
def generate_numbers(n):
    num = 0
    while num < n:
        yield num
        num += 1

total = sum(generate_numbers(l00))

print('total is: ', total)
"""
Maps

* built in Python function used to apply a function to a sequence 
  of elements (list/dictionary)
"""

def square_it_func(a):
    return a * a

x = list(map(square_it_func, [1, 4, 7]))
print(x)

y = [*map(square_it_func, [5, 6, 7])]
print(y) 

