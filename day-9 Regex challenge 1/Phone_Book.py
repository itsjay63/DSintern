#Simpsons Phone Book

"""
    There are some people with the surname 'Neu'. 
    We are looking for a 'Neu', but we don't know the 
    first name, we just know that it starts with a 'J'. 
    Let's write a Python script, which finds all the lines of 
    the phone book, which contain a person with the described 
    surname and a first name starting with 'J'. 
 Hint: 
     Use Regular Expressions 
 
 Output:
     Jack Neu 555-7666
     Jeb Neu 555-5543
     Jennifer Neu 555-3652
"""

"""
fh = open("simpsons_phone_book.txt", 'r')

#read
#readline
#readlines

fh.read()

fh.close()

fh = open("simpsons_phone_book.txt", 'r')

#read
#readline
#readlines

fh.readline()
fh.readline()

fh.close()


fh = open("simpsons_phone_book.txt", 'r')

#read
#readline
#readlines

fh.readlines()


fh.close()



fh = open("simpsons_phone_book.txt", 'r')

for line in fh:
    print (line)

fh.close()
"""
#^J\w*\s*(Neu)

import re

fh = open("simpsons_phone_book.txt", 'r')

for line in fh:
    if (re.search(r'^J\w*\s*(Neu)', line)):
        print (line)


fh.close()






