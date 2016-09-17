import Constants as const
import itertools


def segment(cipher):
    """
    The function segment splits text into a dictionary that consist of column number : string of length 11.
    :param cipher:
    :return: dictionary (int : str)
    """
    global word
    newDict = {}
    newList = []
    column = 1
    for x in range(len(cipher)):
        if len(newList) != 11:
            # Add the elements to the list
            newList.append(cipher[x])
        else:
            # Add the elements to the list
            word = ''.join(newList)
            # Add the list to a dictionary
            newDict[column] = word
            column += 1
            newList = [cipher[x]]
    newDict[column] = word
    permutations(newDict)


def permutations(myDict):
    mylist = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7], 7))
    print myDict.get(1)


segment(const.cipher17)
