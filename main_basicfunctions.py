someNumber = 10

# Step 1: Define the function
def functionThatModifiesNumber(someNumber):
    print("Argument (input) passed in = ", someNumber)
    someNumber = someNumber + 10
    print('After modification, but inside the function, value = ', someNumber)
    return

# Step 2: Call the function
#Before the function calls
print('Value of the variable in calling code before function: ', someNumber)
functionThatModifiesNumber(someNumber)
print('Value of variable in calling code after function: ', someNumber)

someNumber = 11
def functionThatReassignsNumber(someNumber):
    print("Argument (input) passed in = ", someNumber)
    someNumber = 3.14
    print('After re-assignment, but insde the function, value = ', someNumber)
    return

print('Value of the variable in calling code before function: ', someNumber)
functionThatReassignsNumber(someNumber)
print('Value of variable in calling code after function: ', someNumber)

# The above code shows that if a function modifies a numeric argument - no result in the calling code
#Numbers are not mutable by functions

######################################
# A simple function that takes in a circle's radius, returns its area
#####################################################################

# Step 1: Define the function

def calculateAreaOfTheCircle(radius):
    area = 3.14 * radius * radius
    #Now return the area, i.e. send it back to the calling function
    return area

# Step 2: Call the function
radiusOfMyCircle = 5
area = calculateAreaOfTheCircle(radiusOfMyCircle)
print('Radius = ', radiusOfMyCircle, 'Area = ', area)
###################################################
# The following function does not return any value
###################################################
def printAreaOfTheCircle(radius):
    area = 3.14 * radius * radius
    #Now return the area, i.e. send it back to the calling function
    print('Given a circle with radius = ', radius, ' Area = ', area)

####################################################################################
# The following function takes in a list of radii and returns a list of their areas
####################################################################################

# Step 1: Define the function
def calculateAreaOfManyCirclesAllAtOnce(radiusList):
    # Define an empty list to store the results
    resultList = []
    for oneRadius in radiusList:
        resultList.append(3.14*oneRadius*oneRadius)
    return resultList
    
# Step 2: Call the function
listofRadii = [1,2,3,4]
areaList = calculateAreaOfManyCirclesAllAtOnce(listofRadii)
print('For circle with radii = ', listofRadii, ' areas are ', areaList)

#####################################################################################
# The following function that takes in a list of circle radii, then return 2 outputs
# Output 1: List of areas of those circles
# Output 2: List of circumferences of those circles
#####################################################################################

def calculateAreaandCircumference(radiusList):
    areaResultList = []
    circumferenceResultList = []
    resultHash = {'Areas': areaResultList,
                'Circumference': circumferenceResultList}
    for oneRadius in radiusList:
        areaResultList.append(3.14*oneRadius*oneRadius)
        circumferenceResultList.append(3.14*2*oneRadius)

    return resultHash

listofRadii = [1,2,3,4]
resultMap = calculateAreaandCircumference(listofRadii)
print('For circles with radii = ', listofRadii, '\nAreas = ', resultMap["Areas"], '\nCircumference = ', resultMap['Circumference'])