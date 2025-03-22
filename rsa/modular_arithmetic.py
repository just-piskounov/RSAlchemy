"""
modular_arithmetic.py 

This module contains all necessary functions to perform modular 
arithmetic for the RSA applications. This includes everything from
efficient integer multiplication via karatsuba for faster overall computations,
gcd, extended euclide, modular inversion and etc. 

Functions:
    - euclidian_div(a, b) : Performs euclidian division on two integers
    - gcd(a, b) : Computes the gcd of two integers via the euclidian algorithm
    - euclidian_ext(a,b) : Performs the extended euclidian algorithm 
    - mod_inv(a, n) : Finds the modular inverse of an integer modulo an integer 
    - mod_exp(a, e, n) : Performs fast modular expenetiation  
    - chinese_remainders(A, R) : For fast decryption for the RSA
"""

def euclidian_div(a: int, b: int) -> tuple:
    """
    Performs the euclidian division on two given integers
    Returning the quotient and the remainder of the division. The formula 
    is given by a = b * q + r where:
        q is the quotient 
        r is the remainder ( 0 <= r < |b|)

    Args:
        a (int) : The devidend
        b (int) : The devisor 

    Raises:
        ValueError : If the divisor 'b' is zero or if either of 'a' and 'b' are negative 

    Returns:
        tuple : A tuple containing the quotient and the remainder of
        the division :
            q (int) : the quotient of the division 
            r (int) : the remainder of the division 

    Example:
        >>> euclidian_div(10,3)
        (3,1)
    """
    if b == 0:
        raise ValueError("Divisor must not be zero.")

    # Handling the absolute values of a and b
    abs_a = abs(a)
    abs_b = abs(b)

    q = 0
    r = abs_a

    # Division process
    while r >= abs_b:
        r -= abs_b
        q += 1

    # Adjusting the sign of the quotient and remainder
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        q *= -1
        if r != 0:
            r = abs_b - r

    return q, r
def gcd(a: int, b:int) -> int :
    """
        Perform euclid's algorihtm in order to obtain the gcd of two given integers a, b. 

        Args: 
            a (int): the first integer
            b (int): the second integer 

        Raises:
            ValueError : If any of the inputs isn't a positive intger 

        Returns:
            d (int): the value of the greatest common devidor of 'a' and 'b'
        
        Example:
            >>> gcd(20,30) 
            10 
    """

    if (a <= 0) or (b <= 0):
        raise ValueError("The inputs have to be > 0")

    while b != 0 :    # Here we utilize the function we defined previously 
        a, b = b, euclidian_div(a, b)[1]    # We use the fact the the GCD of a, b is the same as a, a%b

    return a    # When b becomes 0, a is the GCD


def euclidian_ext(a: int, b: int) -> tuple:
    """
    Perfoms the extended euclidian algorithm on two given 
    integers. i.e, returns the respective values of u,v and gcd, the 
    values in the bezout identity, where : 
        - u.a + v.b = gcd(a,b) 

    Args : 
        a (int) The first integer
        b (int) The second integer

    Returns : 
        tuple : a tuple containing the values returned by teh extended euclidian 
        algroithm :
            u (int) : 'a' cofficinet in the bezout identity
            v (int) : 'b' cofficinet in the bezout identity
            d (int) : gcd(a,b)
    Example : 
        >>> euclidian_extended(4,11) 
        (3, -1, 1) 
    """
    
    # Coefficient initilization
    u0, v0, u1, v1 = 1, 0, 0, 1

    # The iterations 
    while b != 0:
        q, r = euclidian_div(a, b)
        a, b = b, r 
        u0, u1 = u1, u0 - q * u1 
        v0, v1 = v1, v0 - q * v1

    return a, u0, v0

def mod_inv(a, n) -> int:
    """
    Find the modular inverse of a given integer with respect to 
    a given modulus. Naturally the given integer should be coprime
    with n
    Args:
        a (int) : The given integer to inverse
        n (int) : The modulues

    Returns:
        inv (int) : The modular inverse of a modulus n 

    Raises:
        ValueError : if a is not coprime with n (necessary and sufficient for the existence of the inverse) 
    """
    if gcd(a, n) != 1:
        raise ValueError(f"{a} and {n} are not coprime, the inverse doesn't exist")

    # We simply return the result given by the extended euclid function taken modulo n 
    
    inverse = euclidian_ext(a, n)[0]
    _, inverse = euclidian_div(inverse, n)

    return inverse
def mod_exp(a: int, e: int, n: int) -> int:
    """
    Perform fast modular expenentiation on an a give integer, 
    Utilizing the formula (a mod n) ^ n1) * (a mod n) ^ n2 = 
    (a mod n) ^ (n1 + n2). We will take the expenentation to e/2 
    each time 

    Args: 
        a (int) : the base of the expenentiation, positive integer
        e (int) : the expenent, a signed integer
        n (int) : the modulus of the expenentiation

    Returns: 
        res (int) : the result of the modular expenetiation 

    Example : 
       >>> mod_exp(2,3,5)
        3
    """

    # Base case step : When e = 0 
    if e == 0:
        return 1 

    res = 1    # Initializing the result 

    while (e > 0):
        if ((euclidian_div(e,2)[1] != 0)):
            res *= a 
    
        # We update the value of the exponent 
        e = euclidian_div(e, 2)[0] # The quotient of e by 2
        a = a * a # We update a to a² 

    return euclidian_div (res, n)[1] 

def chinese_remainders(A: list, R: list) -> int:
    """
    This function implements the well known chinese remainders in modular arithmetic, with the main 
    purpose being to get faster decryption for the RSA. The statement of the theorem for clarity 
    and to uniform notatio: Let the system of modular equations for the ai being pairwise coprime : 
    x = m1 mod a1, x = m2 mod a2 .. x = mn mod an has a unique solution mod M, the prodcut of the miA

    Args: 
        A (list): The array of the the modulies ai 
        R (list): The array of the mi 

    Raises:
        ValueError: If the lists aren't equal in size 
        ValueError: If the ai are not mutually coprime 
        ValueError: If one of the input lists are empty

    Returns:
        - x (int): The solution of the system mod the product of the mi
    
    Example:
        >>> chinese_remainders([3, 4, 5], [2, 3, 1])
        11 
    """
    
    if len(A) != len(R) :
        raise ValueError("The number of remainder and modulos is not equal")

    if len(A) == 0 :
        raise ValueError("The input cannot be empty")
    
    for i in range(len(A)):
        for j in range(i + 1, len(A)): 
            if i != j and gcd(A[i], A[j]) != 1:
                raise ValueError("The moduli are not all coprime")

    M = 1   # Computing the product of the mi, i.e M 
    for mi in A:
        M *= mi 

    x = 0   # Computing the result using the formula in the theorem's proof
    for i in range(len(A)):
        ni, _ = euclidian_div(M, A[i])
        _, invi , _ = euclidian_ext(ni, A[i])
        x += R[i] * ni * invi 

    # We return the final result modulo M 
    return euclidian_div(x, M)[1]

