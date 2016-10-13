import Caesar
import Constants as const
import operator


##############################################################################
# Analyze the cipherText and return the recurrence of each character.
# The information is sent to the text file 'myResults.txt'.
##############################################################################


def displayresults(mylist):
    """
    Creates a text file and displays the occurrence of each character in the cypher text.
    :param mylist:
    :return: myResults.txt
    """
    f = open('myResults.txt', 'w')
    f.write(const.intro)
    for x in mylist:
        f.write('\t' + str(x) + '\n')
    f.write(const.explain)
    f.close()


def getdictionary():
    """
    Create an Array of Upper case Letters
    :return: chr Array
    """
    mydict = {}
    for x in range(ord('A'), ord('[')):
        mydict[chr(x)] = 0
    return mydict


def frequency():
    """
    Frequency analyze the string and display the frequency of each character in the string.
    :return: int: shift key
    """
    mydict = getdictionary()
    myarray = list(const.cipherText)
    for x in myarray:
        if x in mydict:
            mydict[x] += 1
    sortmyarray = sorted(mydict.items(), key=operator.itemgetter(1))
    sortmyarray.reverse()
    popular = sortmyarray[0]
    shift = ord(popular[0]) - ord('E')
    displayresults(sortmyarray)
    return shift, sortmyarray


def decipher():
    """
    Appends more information to the 'myResults.txt' file
    :return:
    """
    shift, array = frequency()
    plaintext = Caesar.decrypt(shift)
    with open('myResults.txt', 'a') as f:
        f.write('\n' + plaintext + '\n')

    f.close()


decipher()


