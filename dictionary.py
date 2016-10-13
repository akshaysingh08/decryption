import popular_words as popword
import Constants as const


def countwords(mydict, shift):
    """
    Iterates throughout each tuple in the dictionary and counts the number
    of 'common words' in each string. And only writes the text with the highest
    word count from each shift.
    :param shift:
    :param mydict:
    :return: write to a file 'dictionaryResults.txt'
    """
    triple = {}
    i = 0
    for x in mydict:
        count = 0
        for y in popword.pop:
            if y in mydict[x]:
                count += 1
        triple[i] = (count, x, mydict[x])  # Permutation, count, combination, text
        i += 1
    sortDict = sorted(triple.items(), key=lambda x: x[1][0], reverse=True)
    with open('dictionaryResults.txt', 'a') as f:
        f.write('\n' + 'Shift: ' + str(shift) + '\t')
        q = sortDict[0]
        for r in q:
            if isinstance(r, tuple):
                for a in r:
                    f.write('\t\t' + str(a))
            f.write('\n')
        f.close()
