from rsa.modular_arithmetic import * 

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
        - rsa_dec(c, n, d = None, p = None, q = None)
""" 

def rsa_enc(m, n  ,e = 65537): 
    """
    Performs the RSA encryption on a given word (m), in this case, it has to be coprime with n to ensure the
    bijectivity of the encryption method.

    Args:
        m (int) : The message to be encrypted using the RSA, such that gcd(m, n) = 1
        e (int) : The expoenent of the encryption, to make it more secure, we take 65537 as the default value. e has to be coprime with n
        n (int) : The modulus of the expenetiation. 

    Example:
    >>> rsa_enc()

    """
    
    # We already have the fast modular expenetiation function in the modular_arithmetic module, hence we just use it 

    return mod_exp(m, e, n)

def rsa_dec(c, n, d = None, p = None, q = None):
    """
    Performs the RSA decryption given a cipher message (c) and either the private key (n, d) or 
    the prime facorisation of n.

    Args: 
        c (int) : The cipher text encrypted using the public key (n, e)

    """
    if p != None and q != None:
        if n != p * q:
            raise ValueError(f"Invalid prime facotorization for {n}, {n} != {p} * {q}")

    # If the value of d is not precalculated, we do the precedure using modular_arithmetic module
    if d == None: 
        phi = (p - 1) * (q - 1)  # Euler's tuotient function 
    d = mod_inv(e, phi)

    # We decipher using the chinese remainders theorem for more efficiency (if p and q arent None)
    if p != None and q != None:
        _, dp = euclidian_div(d, p - 1)
        _, dq = euclidian_div(d, q - 1)

        m_p = pow(c, dp, p)
        m_q = pow(c, dq, q)

        A = [p, q]
        R = [m_p, m_q]

        return chinese_remainders(A, R)

    # In the second case we just use regular modular expenentiation
    else:
        return mod_exp(c, d, n)
