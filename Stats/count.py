import pylab as plt
#### Make sure to run this file in Python 2.7 and have Mathplotlib library

mydict = {('V', 7), ('D', 7), ('R', 6), ('K', 6), ('H', 6), ('B', 6), ('W', 5), ('P', 5), ('O', 5), ('L', 5), ('Q', 4),
          ('U', 3), ('I', 3), ('X', 2), ('S', 2), ('E', 2), ('N', 1), ('F', 1), ('G', 1), ('Z', 0), ('Y', 0), ('T', 0),
          ('M', 0), ('J', 0), ('C', 0), ('A', 0)}


def histogramplot(mydict):
    keylist = []
    valulist = []
    for x in mydict:
        keylist.append(x[0])
        valulist.append(x[1])

    letter = []
    letter.extend(range(1, 27))

    plt.xlabel('Character in the alphabet')
    plt.ylabel('Frequency')
    plt.title('Frequency of each character in the cipher text')
    plt.axis([0, 27, 0, 8])
    plt.bar(letter, valulist, align='center')
    plt.xticks(letter, keylist)
    plt.grid(True)
    plt.show()


