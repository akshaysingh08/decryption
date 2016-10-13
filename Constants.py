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
        'Table of Characters and the frequency count.\n\n'

explain = '\nThe analysis shows that the Letter \'V\' and \'D\' are the most frequent\n' \
          'characters in the cypher text. As an attempt to decipher the text I  will \n' \
          'assume the character \'V\' in the cipher represents the character \'E\' in \n' \
          'plain text. Which results in a shift of 17, (ord(\'V\') - ord(\'E\')). The \n' \
          'following string is the result of the cypher text being run in the decrypt \n' \
          'function with a shift of 17. \n\n'

columnintro = 'Function segment rearranges the cipher-text by splitting the text into subsections.\n' \
              'The size of the subsections is dependent of the key value. For example, if the key length \n' \
              'is 7 then the string is divided into seven pieces. Then the function, permutation is\n' \
              'responsible for shuffling all possible combinations of the subsections and saving them\n' \
              'into a dictionary. Next the merge function concatenates the subsections resulting in a plaintext.\n\n' \
              '\t Column Combination \t\t\t Plain Text\n\n' \

dictintro = 'The results of Dictionary analysis from each string at key-length 5. Each string is crossed reference with popular_words.py  \n' \
            'and count is kept of many words are in the text and only the highest word count from each shift is displayed down below ,\n ' \
            'COMMON WORD COUNT\t PERMUTATION \t\t\t TEXT\n\n' \
            ''

alphabet = 26
