# Control 
# Control structures direct the flow of a program using logical statements. 
# For example, conditionals (if-elif-else) allow a program to skip sections of code, 
# and iteration (while), allows a program to repeat a section.

# If statements
# Conditional statements let programs execute different lines of code depending on certain conditions. 

# Boolean Operators 
# boolean operators and, or, not
# These operators are used to combine and manipulate boolean values. 

# Question 
# 1.1 Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining. 
# Write a function that takes in the current temperature and a boolean value telling if it is raining 
# and returns True if Alfonso will wear a jacket and False otherwise. 
# First, try solving this problem using an if statement
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining: 
        return True
    else: 
        return False 

# Note that we'll either return True or False based on a single condition, 
# whose truthiness value will also be either True or False. Knowing this, 
# try to write this function using a single line. 
def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

# While loops 
# To repeat the same statements multiple times in a program, we can use iteration. 
# In Python, one way we can do this is with a while loop. 

# Questions
# 1.2 What is the result of evaluating the following code? 
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0: 
        x = x + 1
    return x / 0

# square(so_slow(5))
# Infinite loop becasue x will always be greater than 0; the x / 0 is never executed. 
# We also know that here! is never printed since the operand so_slow(5) must be evlauted before 
# function square(x) can be called. 

# 1.3 Write a function that returns True if a positive integer n is a prime number and False otherwise. 
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1: 
        return False 
    i = 2
    while n > i: 
        if n % i == 0: 
            return False
        i += 1
    return True 

