###########################################
# A recursive function to reverse a string
###########################################

# Step 1: Define the function
def reverseStringRecursive(someString):
    #First, set up the base case, i.e. the case when function no longer calls itself
    # Here: if the string input is none or length of one, return as-is
    if someString is None:
        return someString
    if(len(someString)) <= 1:
        return someString
    
    # Make recursive call
    return reverseStringRecursive(someString[1:]) + someString[0]

# Call function
myString = 'hello world'

print('The reverse of ', myString, ' is ',reverseStringRecursive(myString))