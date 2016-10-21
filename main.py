from Caesar import decrypt
from column import segment, segment2
from dictionary import countwords
import Constants as const


#####################################################################################
# The purpose of this program is to produces all variations of the cipher text
#   A. Produce a caesar shift of all variations
#   B. Produce key lengths from 1 to 10
# for i in range(1, 11): # length of key
# In order to run faster after I have narrowed down to key length is
# equal to 5. I go into more details in the report.
######################################################################################


key = 5 # To the run the program much faster this iteration is set on the key being 5.
f = open('columnResults.txt', 'w')
f.write(const.columnintro)
f.close()
f = open('dictionaryResults.txt', 'w')
f.write(const.dictintro)
f.close()

for i in range(1, 27):
    cyphertext = decrypt(i)
    if (len(const.cipherText) % key) == 0:
        countwords(segment2(cyphertext, key), i)
    else:
        countwords(segment(cyphertext, key), i)

#####################################################################################
# End of File, look into 'dictionaryResults.txt' & 'columnResults.txt'
# for results. I will go in more detail in report.
#####################################################################################
