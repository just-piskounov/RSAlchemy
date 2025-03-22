# tests/test_modular_arihtmetic.py 
import sys
import os
from bitarray import bitarray # To use bits instead of python booleans 

# Adding the module path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# To showcase a comparision between primality check methods
import time
from math import log
import math # To analyse gauss and Legendre's formulas
import random # Just for the fermat probablistic test
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

# We need the sqrt function from the math module and our own modular arithmetic functions
from math import sqrt 
from rsa.modular_arithmetic import *
import time 
import os


def is_prime(n: int, method = "naive") -> bool:
    """
    This function verifies wether a given number is prime or not using various methods
    of the choice of the user. 
    
    Args: 
        - n (int) : The integers we want to verify wether is prime or not 
        - method (str) : The method to check primality 

    Returns: 
        - boolean : The truth value of primaly, true if the input is prime, otherwise
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
        return True
    
    elif method == "fermat": 
        if n <= 1:
            return False
        if n == 2:
            return True
        if euclidian_div(n, 2)[1] == 0:
            return False
        k = 5 

        # Test k times, k an adjustable parameter
        for _ in range(k):
            a = random.randint(2, n - 2)
            if mod_exp(a, n - 1, n) != 1:   # We use the modular expenetiation from our module
                return False
        return True
    
    elif method == "miller-rabin":
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        # Write n as d*2^r + 1
        r, d = 0, n - 1
        while euclidian_div(d, 2)[1] == 0:
            r += 1
            d = euclidian_div(d, 2)[0] 
        
        k = 5 
        # Test k times, k an adjustable parameter
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = mod_exp(a, d, n)  # Compute a^d % n
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = mod_exp(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

def sieve_of_eratosthenes(limit):
    """
    A function applying the sieve_of_eratosthenes method to get a list of primality values for givne
    integers 


    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False

    return sum(primes)


def init_seed(): 
    """
    This function initalizes a seed for pseu-random generations for RSA keys 
    We use the classic method of using time and padding with operating system 
    information to make it slightly more secure (using time as a seed is a very 
    basic attack to be tested) 
    
    Args: 
        - None 

    Returns: 
        - A seed to genereate a pseu-random random number 

    Example: 
        >>> init_seed()
            70243
    """
    
    # We get 16 random buytes from the system using os
    random_bytes = os.urandom(16)

    # We get the current time in nanoseconds 
    timestamp = int(time.time())

    # We combine both time and the random bytes into a seed (via XOR)
    seed = int.from_bytes(random_bytes, 'big') ^ timestamp 

    return seed

def sieve_with_bitarray(n):
    if n < 2:
        return 0  # No primes below 2

    # Create a bit array of size n+1, initialized to True
    primes = bitarray(n + 1)
    primes.setall(True)
    primes[0:2] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:  # If i is prime
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False

    # Count the number of True values in the bitarray
    return primes.count(True)

n = 100
prime_count = sieve_with_bitarray(n)
print(f"Number of primes ≤ {n}: {prime_count}")

    

def gen_rand_int32(size: int, seed: int) -> int:
    """
    This function generates a random integer given a certain bit size (up to 32 bits)
    it tkae a seed by calling the seeding function defined previously. 
    We use the LGC algorithm for pseu-random number generation

    Args:
        - size (int) : the bit size of the objective psuedo-random number to generate
        - seed (int) : the seed for the 

    Returns:
        - randomint (int) : the pseu-random number to generate 

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
        - size (int): the size in bits (under 32) to generate 

    Returns: 
        - prime (int): a random prime of the given size 

    Example: 
        >>> gen_rand_prime(1, init_seed())
            2
    """
    
    # We generate a random integer first
    n = randint(size ,init_seed())
    
    # since n initself is random, by increamenting we get the nearest upper bounding prime
    while is_prime(n, "fermat") == False:
        n=+1

    return n
    


def num_of_primes(n: int, formula = "gauss") -> int:
    """
    Give the number of primes under a given integer using the formula
    of chouice. It is very straightforward. 


    Args:
        - n (int): the integer that we want to compute how many primes it upper bounds
        - formula (str) : the forumla to be used for compute the output.

    Returns:
        - pi (int): the number of primes below a given number

    Example: 
        >>> num_of_primes(10)
            4
    """
    
    # We simply apply the formulas

    if formula  == "gauss":
        return float(n) / log(n)

    elif formula  == "legendre":
        return float(n) / (log(n) - 1.08366)

    return res

# Example usage of the module functions in the main function 
def main():

    print("===== Example of generating random integers =====")
    print(gen_rand_int32(15, init_seed()))
    print("===== Example of primality check =====")
    print("We use the various methods defined in our functions in order to compare")
    # The integers to check:
    integers = [11, 2, 3, 7753, 15, 2 ** 11 -1, 1559, 18233, 35419, 1000000, 5, 123142231, 2 ** 12 - 1]
    methods = ["naive", "fermat", "miller-rabin"] 
    
    # We put down the primality check methods to compare
    for method in methods:
         start_time = time.time()
         print(f"===== The method used is: " + method + "=====")
         for i, integer in enumerate(integers):
             if is_prime(integer) == True:
                 print(f"The {i + 1}'th integer is prime")
             else: 
                 print(f"The {i + 1}'th integer is not prime")
         finish_time = time.time()
         print(f"Time taken for the {method} method is : {finish_time - start_time}")
    print("===== Showcasing the Gauss and Legendre's Formulas ======")
    
    # Header for the table
    print(
        f"{'| n':<12} | {'Number of Primes pi(n)':<25} | {'Gauss Formula':<15} | {'Legendre Formula':<18} | {'Gauss Ratio':<12} | {'Legendre Ratio':<15} "
    )
    print("-" * 130)

    # Initialize lists to compute mean and standard deviation
    gauss_ratios = []
    legendre_ratios = []
    
    k = 3 # The power of 10 we want to enumate the primes up to 
    # Populate table
    for n in range(1, k):
        num = 10 ** n
        gauss = num_of_primes(num, "gauss")
        legendre = num_of_primes(num, "legendre")

        # We use the seive technique to enumerate the primes, more memory efficient since we utilize bit arrays
        real_num = sieve_with_bitarray(num)

        ratio1 = gauss / real_num
        ratio2 = legendre / real_num

        gauss_ratios.append(ratio1)
        legendre_ratios.append(ratio2)

        print(
            f"| {num:<10} | {real_num:<25} | {gauss:<15} | {legendre:<18} | {ratio1:<12.4f} | {ratio2:<15.4f}"
        )

    # Compute mean and standard deviation for ratios
    gauss_mean_ratio = sum(gauss_ratios) / len(gauss_ratios)
    legendre_mean_ratio = sum(legendre_ratios) / len(legendre_ratios)

    gauss_std_dev_ratio = math.sqrt(
        sum((x - gauss_mean_ratio) ** 2 for x in gauss_ratios) / len(gauss_ratios)
    )
    legendre_std_dev_ratio = math.sqrt(
        sum((x - legendre_mean_ratio) ** 2 for x in legendre_ratios) / len(legendre_ratios)
    )

    # Print summary statistics for ratios
    print("\n===== Mean and Standard Deviation of Ratios =====")
    print(f"Gauss Mean Ratio: {gauss_mean_ratio:.4f}")
    print(f"Gauss Standard Deviation of Ratios: {gauss_std_dev_ratio:.4f}")
    print(f"Legendre Mean Ratio: {legendre_mean_ratio:.4f}")
    print(f"Legendre Standard Deviation of Ratios: {legendre_std_dev_ratio:.4f}")
    
    print("Without including the 10")
    print("Gauss Mean Ratio: ", 0.91340 )
    print("Gauss Standard Deviation of Ratios: ", 0.0332)
    print("Legendre Mean Ratio: " ,1.0182)
    print("Legendre Standard Deviation of Ratios: ", 0.0421)
    

    print("="*5 +" Examples of generating pseudo-random integers and primes" + "="*5)
    print(f"A random integer is {gen_rand_int32(4, init_seed())}")
    print(f"A random prime is {gen_rand_prime32(4, init_seed())}")
    return 
if __name__ == "__main__":  
    main()

