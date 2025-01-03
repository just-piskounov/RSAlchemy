from modular_arithmetic import * 
"""
rsa_algorithm.py 

This module contains the encryption and decryptions algorithms for the
RSA. It is important to know this the plain (textbook if you wish) version 
for the RSA. In practical use, we will use some sort of padding. 
The functions will be given necessay arguments. Hence we will be having flexibility 
in encryption and decryption (for example, instead of the private key, we will be giving 
the integer factorisation of the private key)
    Functions: 
        - rsa_enc(n, e, m)
        - rsa_dec(c, n, d=None, p=None, q=None)
""" 

def rsa_enc(m, e = 65537, n): 
    """
    Performs the RSA encryption on a given word (m), in this case, it has to be coprime with n to ensure the
    bijectivity of the encryption method.

    Args:
        m (int) : The message to be encrypted using the RSA, such that gcd(m, n) = 1
        e (int) : The expoenent of the encryption, to make it more secure, we take 65537 as the default value. e has to be coprime with n
        n (int) : The modulus of the expenetiation. 
    """
    
    # We already have the fast modular expenetiation function in the modular_arithmetic module, hence we just use it 

    return mod

def rsa_dec(c, n, d):
    """
    qriff
    """
    return
