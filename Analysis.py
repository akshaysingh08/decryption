import Caesar
import Constants as const
import operator


##############################################################################
# Analyze the cipherText and return the recurrence of each character #########
##############################################################################


def displayresults(mylist, shift):
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


def frequency():
    """
    Frequency analyze the string and display the frequency of each character in the string.
    :return: int: shift key
    """
    mydict = const.getdictionary()
    myarray = list(const.cipherText)
    for x in myarray:
        if x in mydict:
            mydict[x] += 1
    sortmyarray = sorted(mydict.items(), key=operator.itemgetter(1))
    sortmyarray.reverse()
    popular = sortmyarray[0]
    shift = ord(popular[0]) - ord('E')
    displayresults(sortmyarray, shift)
    return shift


def decipher():
    plaintext = Caesar.decrypt(frequency())
    print plaintext




decipher()