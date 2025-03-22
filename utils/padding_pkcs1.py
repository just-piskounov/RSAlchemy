"""
This module contains the functions necessary to apply paddings on texts (or even chunks from images) 
for RSA encryption (for security, for example to survive attack like the plaintext attack). 

Functions: 
    - pad_pkcs1(plain, key_size)
    - strip_pkcs1(padded)
"""

# We import os to generate the random bytes
import os 

def pad_pkcs1(plain: str, key_size: int) -> str:
    """
    This function applies the pkcs1 padding on a given RSA message in order to encypt the result 
    padded message (since we need the message to be coprime with n, the public key) and also of a 
    proper size. 

    Args:
        - plain (str) : the plain text to be encrypted (it has to be of a relatively small size to ensure the capability for
        - padding) 
        - key_size (int) : the key size (in bytes) for the RSA encryption to ensure text is encrypted securely 
    
    Raises: 
        - ValueError: if the message is larger than the key size for the ecryption 
    Returns:
        - padded (int) : the padded integer as an input for RSA encryption 

    Example: 
        >>> pad_pkcs1("Hello, World!")
            output
    """

    max_length = key_size - 11 
    if len(plain) > max_length:
        raise ValueError("Given message is too long for the RSA key size")

    # We generate the random padding first 
    padding_length = key_size - len(plain)
    
    # Initializing the padding string 
    padding= b""

    while len(padding) < padding_length:
        # We generate one random padding byte by a time from the operating system 
        pad_byte = os.urandom(1)
        if pad_byte != b"\x00": # The padding can't include the byte 0x00
            padding += pad_byte

    # Final contruction of the padded message 
    padded = b"\x00\x02" + padding + b"\x00" + plain.encode("utf-8") 

    return padded
        

def strip_pkcs1(padded: str, key_size: int):
    """
    This function removes the PKCS padding from a padded message (incase we want to decrypt)
    and get the original message, or just as an extra utility 
    
    Args: 
        - padded (str): The given padded string with PKCS1 
        - key_size(int): The RSA key size in bytes 

    Raises:
        - ValueError: if the padded text is not of the right size or doesn't match the padding scheme, or if the separator index is not found

    Returns: 
        - plain (str): The plain text  

    Example: 
        >>> strip_pkcs1()
            output
    """
    
    # We raise an error if the sizes don't match
    if len(padded) != key_size:
        raise ValueError("Invalid padded message length for the given key size")
    
    # We raise an error if the padding scheme is not matched
    if padded[0] != 0x00 or padded[1] != 0x02:
        raise ValueError("The PKCS1 padding scheme is not matched")

    # We find the position of the separtor in the padding scheme (0x00 after the padding string)
    idx = padded.find(b"\0x00", 2)
    if idx == -1:
        raise ValueError("The padding seperator is not found")

    # We simply extract the plaintext according to the PKCS1 padding scheme
    plaintext = padded[idx +1:]

    return plaintext
    
def main():
    print("===== Example of a padded message ======")
    print(pad_pkcs1("Hello, World!", 50))
    
    print("===== Example of stripping off the padding")
    return 
    print(strip_pkcs1(pad_pkcs1("Hello, World!", 50)))
if __name__ == "__main__":
    main()
