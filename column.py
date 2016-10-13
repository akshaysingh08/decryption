import itertools
import Constants as const


#######################################################################################################
# Function segment rearranges the cipher-text by splitting the text into subsections.
# The size of the subsections is dependent of the key value. For example, if the key length
# is 7 then the string is divided into seven columns of equal length (Additional method is call
# to implement method, if needed). Then the function permutation is  responsible for shuffling all
# possible combinations of the subsections and saving them into a dictionary. Next the merge function
# concatenates the subsections resulting in a plaintext. And Finally the plaintext is sent to
# dicionary.py for word analysis.
#######################################################################################################

def segment(cipher, key):
    """
    The function segment splits text into a dictionary that consist of column number : string of length
    (length of cipher/key). CipherText needs Padding.
    :param key: int
    :param cipher: str
    :return: dictionary (int : str)
    """
    cipherList = []
    newDict = {}
    newList = []
    column = 1

    if len(cipher) % key != 0:
        cipherList = list(cipher)
        dictindex, index = dicpad(key)
        for i in index:
            cipherList.insert(dictindex[i], '?')
    cipher = ''.join(cipherList)

    for x in range(len(cipher)):
        if len(newList) != (len(cipher) / key):
            newList.append(cipher[x])
        else:
            word = ''.join(newList)
            newDict[column] = word
            column += 1
            newList = [cipher[x]]
    word = ''.join(newList)
    newDict[column] = word
    results = permutations(newDict, key)
    displayresults(results)
    return results


def segment2(cipher, key):
    """
    The function segment splits text into a dictionary that consist of column number : string of length
    (length of cipher/key). CipherText does not need padding.
    :param key: int
    :param cipher: str
    :return: dictionary (int : str)
    """
    global word
    newDict = {}
    newList = []
    column = 1
    for x in range(len(cipher)):
        if len(newList) != (len(cipher) / key):
            newList.append(cipher[x])
        else:
            word = ''.join(newList)
            newDict[column] = word
            column += 1
            newList = [cipher[x]]
    newDict[column] = word
    results = permutations(newDict, key)
    displayresults(results)
    return results


def permutations(myDict, key):
    """
    Creates all permutations from the dictionary.
    :param key:
    :param myDict:
    :return: a dictionary { column order : plaintext}
    """
    pc = {}
    newDict = {}
    mylist = list(itertools.permutations(createarray(key), key))
    for x in mylist:
        sentence = []
        for y in x:
            sentence.append(myDict[y])
        pc[x] = sentence
    for x in pc:
        stringlist = pc[x]
        string = merge(stringlist)
        newDict[x] = string
    return newDict


def createarray(key):
    """
    Creates an array from 1 to key.
    :param key:
    :return: array of integers
    """
    array = []
    for i in range(1, key + 1, 1):
        array.append(i)
    return array


def merge(mylist):
    """
    Concatenates a list of strings into one long string.
    :param mylist:
    :return: str plaintext
    """
    string = ''
    for i in range(len(mylist[0])):
        for x in mylist:
            if x[i] is not '?':
                string += x[i]
    return string


def displayresults(mylist):
    """
    Takes the object of type list and writes all entries onto a text file.
    :param mylist:
    :return: none
    """
    with open('columnResults.txt', 'a') as f:
        for x in mylist:
            f.write('\t' + str(x) + '\t: ' + str(mylist[x]) + '\n')
    f.close()


def dicpad(key):
    """
    Produce the a list of possible indexes where padding can be place
    into the ciphertext to conclude a columnar shift.
    :param key:
    :return:
    """
    indexdict = {}
    for x in range(1, key + 1):
        indexdict[x] = (x * 16) - 1
    index = [1, 2, 4]
    return indexdict, index
