# tests/test_modular_arihtmetic.py 
import sys
import os

# Adding the module path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from rsa.modular_arithmetic import * 

def test_euclidian_div():
    """
    Test the euclidian division function
    In multiple cases, where both integers are positive,
    where divedend is smaller than the devisor, and 
    where the exception condition is met
    """
    # Positive dividend and divisor
    assert euclidian_div(7, 3) == (2, 1)
    assert euclidian_div(10, 5) == (2, 0)
    
    # Dividend smaller than divisor
    assert euclidian_div(2, 5) == (0, 2)

    # Divisor cannot be zero
    with pytest.raises(ValueError):
        euclidian_div(7, 0)

def test_gcd(): 
    """
    Test the gcd function 
    """

    assert gcd(13,26) == 13
    assert gcd(13*9*11, 9*11) == 9 * 11 

    assert gcd(12, 56) == 4

def test_euclidian_ext():
    """
    Test the extended euclid's algorithm 
    """
    # Standard cases
    assert euclidian_ext(4, 11) == (1, 3, -1)
    assert euclidian_ext(11, 4) == (1, -1, 3)
    assert euclidian_ext(14, 30) == (2, -2, 1)
    
    # Edge cases with one number being zero
    assert euclidian_ext(0, 7) == (7, 0, 1)
    assert euclidian_ext(7, 0) == (7, 1, 0) 

    #Larger inputs
    assert euclidian_ext(12345, 54321) == (3, 3617, -822)
    
    # Check if Bézout's identity holds for all cases
    gc, u, v = euclidian_ext(4, 11)
    assert u * 4 + v * 11 == gc
    
    gc, u, v = euclidian_ext(14, 30)
    assert u * 14 + v * 30 == gc
    
    gc, u, v = euclidian_ext(12345, 54321)
    assert u * 12345 + v * 54321 == gc

def test_mod_exp_basic():
    """
    Test for the modular expenentiation function
    """
    assert mod_exp(2, 3, 5) == 3
    assert mod_exp(3, 3, 7) == 6
    assert mod_exp(5, 0, 13) == 1
    assert mod_exp(4, 2, 5) == 1

def test_chinese_remainders():
    """
    Test for the chinese remainders function 
    """
    assert chinese_remainders([3, 4, 5],[2, 3, 1]) == 11 


