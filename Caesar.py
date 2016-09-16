import Constants as const


########################################################################################################################
# Caesar.py
# Author: Juan Navarrete
# Implement a Caesar Cipher, where characters in a string are shift a certain number of places down or up the alphabet.
# The mathematical formula   for encryption is e(x) = (x + h) (mod 26)
# Where x is the plaintext character and h is a shift in alphabet.
# The mathematical formula for decryption is e(x) = (x - h) (mod 26)
########################################################################################################################

def encrypt(text, shift):
    """
    Encrypt plaintext into a cipher text. Shifts each character down the ascii table
    by the shift argument.
    :param text:
    :param shift:
    :return: str: encrypt
    """
    earray = []
    myarray = list(text)
    for x in myarray:
        a = (ord(x) + (shift % const.alphabet))
        if a > ord('Z'):
            a = (a % ord('Z')) + 64
        b = chr(a)
        earray.append(b)
    return ''.join(earray)


def decrypt(shift):
    """
    Decrypt cypher text into plain text. Shifts each character up the ascii table
    by the shift argument.
    :param shift:
    :return: str: plaintext
    """
    erray = []
    myarray = list(const.cipherText)
    for x in myarray:
        a = (ord(x) - (shift % const.alphabet))
        if a < ord('A'):
            a += const.alphabet
        b = chr(a)
        erray.append(b)
    return ''.join(erray)


