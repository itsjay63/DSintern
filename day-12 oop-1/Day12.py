"""
where will be the memory allocated in ram and how much?
depends on compiler ... also depends on microprocessor 
stack 

in python memory allocated at two places stack and heap 
stack contains address of data and heap contains the value of data 

while in other languages data value store in the stack itself.
"""
#--------------------------------------------------------------------
# How the memory is allocated in C Language 
# Use of & addressof operator to find the address
# int a = 6 ;
# &a

# How the memory is allocated in Python Language 
a = 6
print(id(a)) #it will return stack address 


# Introduce the concept of Reference Count
b = 6
print(id(b)) 
print(id(a))
#here a and b are reference variable because they store reference(address) of data 
#values within heap is called object 

# Everything in Python is class
a = 6 # class int 
#a = 10.7 # class float 
#a = "Forsk" # class str
#a = True #class bool 
#a = None #class NoneType

print(type(a))
print(a.__class__)

# If primary data types are class then we can create objects
b = int()
print(b)
print(type(b))


c = int(7)
print(c)
print(type(c))

# Summary
# datatype = you create a variable of it
# Class    = you create a object of it 
# Difference between Reference Variable and Object

# OOPS is Object Oriented Programming System
# OOD  is Object Oriented Design


# History of Software Development 
"""
1950 - First OS ( Assembly Language - high level)
1960 - Fortran, Algol, Cobol, Basic
1964 - OS/360 Mainframe
1967 - Simula (OOP)
1970 - C / Unix
1991 - Linux 

Procedural - Routines / Sub routines / Function and variables
Procedural ( Data and Function as seperate entities)

Why was OOP Invented ?

Slow
Expensive
Time Consuming

Maintainability
Extensibility
Reusability
DRY ( Do not repeat yourself)

OOPS is a philosophy and not a language 
It Logically group data and function 
Easy to reuse and build upon complex softwares
"""


# Introducing the keywords of Object Oriented Programming
"""
Class
Object/Instance
Data Hiding   
    Abstraction     - Something only existing as an idea
    Encapsulation   - Restricts access 
    Inheritance     - Create a new from existing
    Polymorphism    - Object that have more than 1 form 
Overriding 
Overloading
"""

# Algorithm to convert any real world object into class

"""
# Steps for converting a REAL LIFE OBJECT into a CLASS
# 1. Visualise the REAL LIFE OBJECT in your memory 
# 2. List down the characteristics/state of the object
# 3. List down the Functionality/Behaviour of the object 



# Introduce the concept of Radio Blueprint 

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------
Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)
class name = Real world object name = radio 
8 variables 
4 functions
"""
#-----------------------------
"""     
Represent Employee in Python 
Individual employee will have specific attributes and methods
Name
email address
Pay

Each individual employee would be the instance of the class 
"""

class Employee:
    pass #at this moment i dont know what to put in my class, also it avoid error 

emp_1 = Employee()
#emp_1 is known as reference variable
#memory allocation stack
#create an object of employee in heap 
#stores the address in the ref variable 
emp_2 = Employee()


print ( emp_1)     # 0x115b68b00
print ( id(emp_1)) # 4659251968

print ( emp_2)
print ( id(emp_2))


