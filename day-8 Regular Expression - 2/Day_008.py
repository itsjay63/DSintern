#regular exp , also find sub strings

import re

dir(re)

"""
sub
findall
search
match
compile
"""

s = 'aaa@gmail.com bbb@yahoo.com ccc@outlook.com'

#'ABC@gmail.com ABC@yahoo.com ABC@outlook.com'
#re.sub('expression','want to replace',source)
sub_s = re.sub('[a-z]*@','ABC@',s)


str1 = 'bluepink123abc123xyz456_0'
#re.findall('expression',source)
#findall find all the matching string and return as a list 

re.findall('\d\d\d', str1) #['123','123','456']
re.findall('^\d\d\d', str1) #[]


str1 = 'foo123bar456'
#re.search('expression',source)
#search method return index .... span=(3,6) 
re.search('\d\d\d' ,str1)


str2 = 'Forsk forsk coding School'

re.match('forsk', str2) # blank output 
re.search('forsk', str2) #return index 


re.match('Forsk', str2) #return index
re.search('Forsk', str2) #return index
#search ⇒ find something anywhere in the string and return a match object. 
#match ⇒ find something at the beginning of the string and return a match object

#version 01
str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in Sylvester Drishaym2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'

re.findall('\w+@\w+\.\w+', str1 )


#version 02
str1 = 'kisan andolan forsklabs@gmail.com 1234 yogendra@forsk.in Sylvester Drishaym2 yogendrasingh@qualcomm.com mohanlal ysingh@mango.com covid yogendra@zdrv.com'
#compile just use for , we do not have to write things again and again 
epattern = re.compile(r'\w+@\w+\.\w+') #r is stands for row string 
epattern.findall(str1 )

#example for row string 
#print('a\tb') #a    b
#print(r'a\tb') # a\tb , it will print as it is.





