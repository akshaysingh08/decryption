##############################################################################
# Constants values and strings are stored here for aesthetics ################
##############################################################################

cipherText = 'DRPWPWXHDRDKDUBKIHQVQRIKPGWOVOESWPKPVOBBDVVVDXSURWRLUEBKOLVHIHBKHLHBLNDQRFLOQ'
intro = 'myResults.txt displays the frequency of each character in the cipher text.\n' \
        'The most frequent letter in cipher text will represent the letter \'E\'. In\n' \
        'English, the letter \'E\' is the most common character in the alphabet. This\n' \
        'information is crucial in calculating the shift in the Caesar cipher. To \n' \
        'calculate the shift is the difference between the ascii value of the most \n' \
        'frequent letter and the ascii value of \'E\'.\n' \
        '\n' \
        'Table of Characters and the frequency count.\n'

explain = ''

alphabet = 26


def getdictionary():
    mydict = {}
    for x in range(ord('A'), ord('[')):
        mydict[chr(x)] = 0
    return mydict

