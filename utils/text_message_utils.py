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
    """
    
    int_txt = ''.join([str(ord(i)) for i in text])   # Simply we join the ASCII of composing characters to get an integer
    
    return int_txt

def bytes_to_long(int_msg: int) -> str:
    """
    This function does the opposite convertion of long_to_bytes. i.e given an integer it converts back 
    to a string (usually after the RSA decryption), with each carachter correspoding the asccii value of the the byte in the same position 

    Args: 
        int_msg (int): The message in its integer form 

    Returns: 
        text_msg (int): The message back into its text (ASCII) form 

    Example: 
        >>> bytes_to_long()
            Hello, World!
    """

    # We put down the binary representation of our integer information 
    
    binary_rep = bin(int_msg[2:0]) # To remove the 0b prefix 

    # Initializing the text result 
    txt_msg = ""
    for i in range(0, len(binary_rep), 8):    # A step of 8 bits at a time 
        byte = binary_rep[i, i + 8] 
        text_msg += chr(int(byte, 2))   # Converting the byte into an integer and taking the correspoding ASCII value

    return text_msg
