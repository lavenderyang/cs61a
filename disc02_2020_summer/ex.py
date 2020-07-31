# HOF
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# Lambda Expressions 
what = lambda x: x + 5
what 

(lambda y: y+ 5)(4)
(lambda f, x: f(x))(lambda y: y + 1, 10)

# Currying
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

curried_pow(2)(3)

# Question 1.2 Write curry2 as a lambda function. 
curry2 = lambda h: lambda x: lambda y: h(x, y)


# Question 1.5 
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2. 
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while n >= i: 
        if cond(i): 
            print(i)
        i += 1

# Question 1.6
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all itnegers 1..i..n where calling cond(i) returns True. 

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2. 
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keep_ints(cond):
        i = 1
        while n >= i: 
            if cond(i):
                print(i)
            i+= 1
    return keep_ints 

# Self Reference 
def print_all(x):
    print(x)
    return print_all

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

# Question 1.7 Write a function print_delayed delays printing its arugment until the next function call print_delayed takes in an argument x and returns a new function delay_print. 
# When delay_print is called, it prints out x and returns another delay_print. 
def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behaviour. 

    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >> f = f(4)(5)
    3
    4
    >>> f("h1")
    5
    <function print_delayed> # a function is returned 
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


    # Question 1.8 Write a function print_n that can take in an integer n and return a repeatable print function that can print the next n parameters. 
    # After the nth parameter, it just prints "done". 
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0: 
            print("done")
        else: 
            print(x)
        return print_n(n - 1)
    return inner_print