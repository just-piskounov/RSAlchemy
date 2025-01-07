# We need the sqrt function from the math module and our own modular arithmetic functions
from math import sqrt 
from rsa.modular_arithmetic import *
import time 
import os

"""
This module contains various utility functions that will be needed for a functional RSA implementation 
Since everything is built from scratch, usual utility functions conccerning primes in perticumar are
needed, we provide them in this module

Function: 
    - is prime(n, method) : given an integer and a method, this functions applies a primality 
    check on the given integer 
    - init_seed() : for seed initializeation in order to generate pseu-random numebrs
    - gen_rand_int(bits) : given a certain size (in bits) the function generates a random integer
    - gen_rand_prime(bits) : given a certain size (in bits) the function generates a random prime number 
    -  
"""

def is_prime(n: int, method = "naive": str) -> bool:
    """
    This function verifies wether a given number is prime or not using various methods
    of the choice of the user. 
    
    Args: 
        n (int) : The integers we want to verify wether is prime or not 
        method (str) : The method to check primality 

    Returns: 
        boolean : The truth value of primaly, true if the input is prime, otherwise
        false 

    Example: 
        >>> is_prime(53) 
            True 

        >>> is_prime(3423412)
            False
    """
    # Basic values
    if n in [0, 1]:
        return False 

    if n in [2, 3]:
        return True
    
    # Basic cases eliminiation 
    if euclidian_div(n, 2)[1] == 0 or euclidian_div(n, 3)[1] == 0:    # Divisiblity by 2 and 3
        return False 

    # We perform the test depending on the primality check method
    
    if method == "naive":
        # We check if there are any prime deviders ( they come of the form 6 * k (+ or -) 1 , where k is an integer) 
        # initilizing the index to 5 
        i = 5 
        while i*i <= n: 
            if euclidian_div(n, i)[1] == 0 or euclidian_div(n, i + 2)[1] == 0:
                return False
            i += 6    # We increament by a step of 6
        return False
    
    # The rest of the methods are under developpement
    #elif method == ""


    #return True

def init_seed(): 
    """
    This function initalizes a seed for pseu-random generations for RSA keys 
    We use the classic method of using time and padding with operating system 
    information to make it slightly more secure (using time as a seed is a very 
    basic attack to be tested) 
    
    Args: 
        None 

    Returns: 
        A seed to genereate a pseu-random random number 

    Example: 
        >>> init_seed()
            70243
    """
    
    # We get 16 random buytes from the system calls using os
    random_bytes = os.urandom(16)

    # We get the current time in nanoseconds 
    curr_time = int(time.time(1e9))

    # We combine both time and the random bytes into a seed (via XOR)
    seed = int.from_bytes(random_bytes, 'big') ^ timestamp 

    return seed

    

def gen_rand_int32(size: int, seed: int) -> int:
    """
    This function generates a random integer given a certain bit size (up to 32 bits)
    it tkae a seed by calling the seeding function defined previously. 
    We use the LGC algorithm for pseu-random number generation

    Args:
        size (int) : the bit size of the objective psuedo-random number to generate
        seed (int) : the seed for the 

    Returns:
        randomint (int) : the pseu-random number to generate 

    Example:
        >>> gen_rand_int(5): 
            31
    """
    if size > 32:
        size = 32    # Size limit is 32 bits 
    # We define the LGC constants 
    modulus = mod_exp(2, 32, 1)
    multiplier = 1664525
    increment = 1013904223
    
    # Generation 
    state = seed % modulus 
    state = (multiplier * state + increment) % modulus
    
    # We return the number limited to the desired bit length 
    return state >> (32 - bits)

def gen_rand_prime32(size: int, seed: int) -> int:
    """
    Returns a random prime number via the random generating function 
    Via trial. We generte random integers using the functions we defineed previously
    till we get a prime using primality check 

    Args: 
        size (int): the size in bits (under 32) to generate 

    Returns: 
        prime (int): a random prime of the given size 

    Example: 
        >>> gen_rand_prime(1, init_seed())
            2
    """

def num_of_primes(n: int, formula = "gauss": str) -> int:
    """
    Give the number of primes under a given integer using the formula
    of chouice. It is very straightforward. 


    Args:
        n (int): the integer that we want to compute how many primes it upper bounds
        formula (str) : the forumla to be used for compute the output.

    Returns:
        pi (int): the number of primes below a given number

    Example: 
        >>> num_of_primes(10)
            4
    """
    
    # We simply apply the formulas

    if method == "gauss":
        return n / log(n)

    elif method == "legendre":
        return n / (long(n) - 1.08366)

    return res
