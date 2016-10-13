# decryption
Decrypt a cypher string encrypted with a combination of columnar transposition and simple shift substitution.

Author: Juan Navarrete
Class:  Comp 424: Security


You intercepted a single ciphertext. Decipher it as much as you can. To receive full or partial credit you must show
all your work. Attach any code you have implemented (you can use any programming language) or any code you
have found anywhere that is publicly online (but you must include citations of all sources you used in the report).
DRPWPWXHDRDKDUBKIHQVQRIKPGWOVOESWPKPVOBBDVVVDXSURWRLUEBKOLVHIHBKHLHBLNDQRFLOQ
You may assume you already know:
• The encryption/decryption algorithm is a combination of columnar transposition and simple shift substitution.
• The key length is less than or equal to 10 letters long.
• The original message is in English.
• The original message contains only letters (i.e., no punctuation marks, numbers, etc)


After Running the algorithm I found the key is length 5 (3, 5, 2, 1, 4) and the plain text:
"BE HAPPY FOR THE MOMENT THIS MOMENT IS YOUR LIFE BY KHAYY AMOHANDAL SO THIS CLASS IS REALLY FUN"


COMMON WORD COUNT	 PERMUTATION 			 TEXT
Shift: 3
		47		(3, 5, 2, 1, 4)		BEHAPPYFORTHEMOMENTTHISMOMENTISYOURLIFEBYKHAYYAMOHANDALSOTHISCLASSISREALLYFUN