# tests/test_modular_arihtmetic.py 
import sys
import os
import pytest 
# Adding the module path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from rsa.rsa_algorithm import *

def test_rsa_enc():
    """
    Test function for the rsa encryption function 
    """
    
    # Encryption with already known output values
    assert rsa_enc(2, 33, e = 7) == 29

    # For larger values, and e supposed known 
    assert
    

def test_deterministic():
    """
    Test the determinstic nature of the RSA algorihtm 
    """


