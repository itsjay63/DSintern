# Shopping List App 

"""
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT 
    the program
    And once i quit, I want the app to show me 
    everything thats
    on my list.

Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use 
    the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""

print("what should we pick at the store?")
print("enter DONE to stop adding items in the list")

iteml=[]
while(True):
    i=input("Add item:")
    if(i=='DONE'):
        break
    iteml.append(i)
 
print("Here's you list")
l=len(iteml) 

#for i in range(0,l):
#    print(item[i])

for item in iteml:
    print(item)






