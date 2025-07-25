print('Hello World')

def inputData(fname, lname,birthYear):
    '''Does not return any values, 
    takes three parameters, first name, last name and birth year
    calculates a persons age based on their birth year
    finally will print everything out'''
    byStr = birthYear
    #converting the string to an int
    birthYear = int(birthYear)

    birthYear = birthYear 

    #eval is asking python to guess what the data type is
    evalTest = eval(byStr)

    currentYear = 2025
    age = currentYear - birthYear

    #printing integers here works fine because it is passed as an argument / parameter
    print(lname,',',fname, birthYear)
    #have to convert the int to a string in order to make it part of a string
    print('Hi, my name is '+fname+' '+lname+' I am '+str(age)+' years old')

def myConditional(temp):
    if temp > 86:
        #only will execute if the conditional is true
        print('Hey its hot out')
        print()
        print('hi there white space')
    else:
        #only executes if the conditional is false
        print('its not that hot, maybe I\'ll go have some coffee')

    print('I will check to see if it\'s raining')

def inputLoop(myText):
    
    shouting = ''
    #traditional approach
    #for crazyWeirdVariableName in myText:
    for c in myText:
        if c.islower():
            shouting += c.upper()
        else:
            shouting += c
    return shouting

def rangeLoop():
    lst = [1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me', ['PascalCase', 'camelCase', 'me', "Brian O'Donnell"]]
    #in a range of values
    for i in range(5,len(lst),1):
        print('Index is: '+str(i))
        print('item is:'+str(lst[i]))



rangeLoop()
myConditional(100)
winterWeather = 20
myConditional(winterWeather)
myText = input('Enter some text: ')
myUpperText = inputLoop(myText)
print(myUpperText)
#these three lines do the same thing.  Both effectively capture input
# myFirstName = input('Enter your first name: ')
# print('Enter your last name: ')
# myLastName = input()
# myBirthYear = input('When were you born? ')

#specify which parameter goes with which value
#inputData(birthYear=myBirthYear,fname=myFirstName, lname=myLastName)

#parameters go in the order the function was declared
# inputData(myFirstName, myLastName,myBirthYear)

lst = [1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me', ['PascalCase', 'camelCase', 'me', "Brian O'Donnell"]]

lst[5] = 'SuperCase'