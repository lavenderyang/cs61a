# A good example of recursive function is the factorial funciton. 
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n-1)

# Question 1.1
# Write a funciton that takes two numbers m and n and returns their product. 
# Assume m and n are positive integers. Use recursion, not mul or *! 
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    assert m > 0, "m must be a positive integer."
    assert n > 0, "n must be a postive integer."
    if n == 1: 
        return m
    else: 
        return m + multiply(m, n - 1)

# Question 1.2 
# Below is the iterative version of is_prime, which returns True if positive integer n is a prime number and False otherwise. 
def is_prime_iter(n):
    if n == 1: 
        return False
    k = 2
    while k < n: 
        if n % k == 0: 
            return False
        k += 1
    return True
# Implement the recusive is_prime function. 
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(divisor):
        if n == divisor:
            return True
        elif n == 1 or n % divisor == 0:
            return False 
        else: 
            return prime_helper(divisor + 1)
    return prime_helper(2)

# Tree Recursion
# Consider a function that reqruies more than one recursive call. A simple exmaple is the recursive fibonacci function: 
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n - 1) + fib(n -2)

# Questions 2.1 
# You want to go up a flight stairs that has n steps. You can either take 1 or 2 steps each time. How many different ways can you go up this flight of stairs?
def count_stair_ways(n):
    if n == 1: 
        return 1
    elif n == 2: 
        return 2
    else: 
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_stair_ways_2(n):
    if n == 0: 
        return 1
    elif n < 0: 
        return 0
    return count_stair_ways_2(n-2) + count_stair_ways_2(n-1)

# Question 2.2 
# Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time.
def count_k(n, k):
    """
    >>> count_k(3, 3) 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 0: 
        return 1
    elif n < 0: 
        return 0
    else: 
        i, total  = 1, 0
        while i <= k: 
            total += count_k(n - i, k)
            i += 1
        return total 
   