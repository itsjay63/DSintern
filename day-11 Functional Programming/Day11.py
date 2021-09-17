"""

list1 = [1,2,3,4,5]

#[1,4,9,16,25]

list2 = []
for item in list1:
   list2.append(item*item)

print (list2)

#shortcut
#list comprehension
[item**3 for item in list1]
print ([item*item for item in list1])

list1 = ['Amar','Akbar','Anthony']
#length of  each world in a list
#[4,5,7]


print ([len(name) for name in list1])



list1 = [10,20,30,40]

#[100,400,900,1600]
def squarevalue(x):
  return (x*x)

#print (list(map(squarevalue,list1)))

#map is more efficient than loop 


list1 = [1,2,3,4,5]

def iseven(x):
  return (x % 2 == 0)

print  (list(map(iseven, list1)))

print  (list(map(lambda x:x % 2 == 0, list1)))


print  (list(filter(lambda x:x % 2 == 0, list1)))

#fuctional programming language : in fuctional programming language you can use funtion as a parmeter 
while calling another function 
c and c++ are not fucntional programming language
but this is just a half truth 
in complete functional programming language.... there is no concept of looping 
so python is partial functional programming language 
scala , R ... complete fucntional programming language(use recursion instade of loop )



list1 = [1,2,3,4,5]

def fadd(x,y):
  return (x*y)

import functools

print (functools.reduce(fadd, [1,2,3,4,5]))

print (functools.reduce(lambda x,y: x+y, [1,2,3,4,5]))

"""

#dictionary


"""
name: Bharat
chem: 67
phy: 78
math: 87
"""
dict1 = {
  'name':'Bharat',
  'chem': {'midterm': {'mt1': 40, 'mt2':37}, 'final': 50},
  'phy':78,
  'math':87
}
#dict1[key]=value to update value
#del dict1[key] to del key value pair 
# keys cant be duplicate, values can 
#dict1.keys() it will show all the keys 
#dict1.values() it will show all the values 
#dict1.clear() it will clear all the record from dict1
#dict1['chem']['mt1']

#unpacking
x,y = (6,2)
x, y = divmod(32,5)

t1 = (1,2,3,4,5)

#tuples are read only





