import Constants as const
import itertools


# Function segment rearranges the cipher-text by splitting the text into subsections.
# The size of the subsections is dependent of the key value. For example, if the key length
# is 7 then the string is divided into seven pieces. Then the function, permutation is
# responsible for shuffling all possible combinations of the subsections and saving them i
# nto a dictionary. Next the merge function concatenates the subsections resulting in a plaintext.


def segment(cipher, key):
    """
    The function segment splits text into a dictionary that consist of column number : string of length
    (length of cipher/key).
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
    global sentence
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
            string += x[i]
    return string


def displayresults(mylist):
    f = open('columnResults.txt', 'w')
    f.write(const.columnintro)

    for x in mylist:
        f.write('\t' + str(x) + '\t: ' + str(mylist[x]) + '\n')

    f.close()

#segment(const.cipher17, 7)
