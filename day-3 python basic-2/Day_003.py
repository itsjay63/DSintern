str1 = "Forsk Coding School"
type(str1)
print (len(str1))
#indexing
str1[0]
str1[-1]

#slicing
str1[0:10]
str1[5:15]
str1[10:]
str1[:10]

str1 = "Forsk Coding School"

#string operations
#convert the str1 text to all uppercase

print (dir(str)) #to get list of funtions
help(str.upper) #to know the use of that function , here it will create a copy of str , strings are immutable 
str2 = str1.upper()

str1[0] = 'f'
#strings are read only
#immutable

#import lib/module
import math 
dir(math)
help(math.sqrt)
x = input("Enter the number: ")
x = int(x)
print (math.sqrt(x))

#loops while and for
#version 01
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..leaving app')
        break #terminates the loop
    
    x = int(x)
    
    print (math.sqrt(x))    
    
#version 02
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        print ("the square root is", math.sqrt(x)) 
    else:
        print ("the length is", len(x))


#version 03

datastore = [] #empty list 
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        datastore.append(math.sqrt(x))
    else:
        datastore.append(len(x))



print (datastore)








