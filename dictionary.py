import Constants as const
import column


# count the number of common words in the text
def countwords(mydict):
    """
    Iterates throughout each tuple in the dictionary and counts the number
    of 'common words' in each string.
    :param mydict:
    :return:
    """
    triple = {}
    i = 0
    for x in mydict:
        count = 0
        for y in const.commonwords:
            if y in mydict[x]:
                count += 1
        triple[i] = (count, x, mydict[x])
        i += 1
    sortDict = sorted(triple.items(), key=lambda x: x[1][0], reverse=True)
    f = open('dictionaryResults.txt', 'w')
    f.write(const.dictintro)
    for q in sortDict:
        for r in q:
            if isinstance(r, tuple):
                for a in r:
                    f.write('\t\t' + str(a))
            #else:
            #    f.write('\t' + str(r) + '\t')
        f.write('\n')
    f.close()


#countwords(column.segment(const.cipher_1, 7))
countwords(column.segment(const.cipher17, 7))