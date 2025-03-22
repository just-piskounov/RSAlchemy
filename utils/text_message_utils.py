"""
This modules contains utilities and helper functions for text encryption using the RSA.
We build these functions from scratch, while they do exist in modules like pycryptodome, 
take (bytes_to_long) for example. However to deepen understanding for the functionalities for 
the RSA cryptosystem and the entire logic of it, we implement these utils ourselves using only
built in functions in Python.

Function: 
    - long_to_bytes : converts a text into an integer to encrypt using the RSA
    - bytes_to_long : converts an integer back to its utf-8 text encoding
"""

def long_to_bytes(txt: str) -> int:
    """
    This function converts a text message into an integer by slicing it into bytes, 
    and giving each the correspoding numerical value. Since this is for edcuational 
    purpposes, we build it ourselves even though it exists in libraries like pycryptodome

    Args:
        txt (str) : the text message we want to encrypt using the RSA 
    
    Returns: 
        int_txt (int) : the integer resulting from trasforming the given text into bytes

    Example: 
        >>> long_to_bytes("Hello, World!")
            7210110810811144328711111410810033
    """
    
    int_txt = ''.join([str(ord(i)) for i in txt])   # Simply we join the ASCII of composing characters to get an integer
    
    return int_txt

def bytes_to_long(value: int) -> str:
    """
    This function does the opposite convertion of long_to_bytes. i.e given an integer it converts back 
    to a string (usually after the RSA decryption), with each carachter correspoding the asccii value of the the byte in the same position 

    Args: 
        value (int): The message in its integer form 

    Returns: 
        text_msg (int): The message back into its text (ASCII) form 

    Example: 
        >>> bytes_to_long(7210110810811144328711111410810033)
            Hello, World!
    """

    # We put down the binary representation of our integer information 
    byte_array = value.to_bytes((value.bit_length() + 7) // 8, 'big')
    
    # Convert each byte to its ASCII representation
    ascii_string = ''.join(chr(byte) for byte in byte_array)
    
    return ascii_string 

def main():
    print("===== the string /Hello, World!/ in an integer format")
    print(long_to_bytes("Hello, World!"))

    print("===== Showing that we retreive the integer information back ======")
    print(bytes_to_long(7210110810811144328711111410810033))


    return 

if __name__ == "__main__":
    main()
