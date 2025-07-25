print('Hello World')


#these three lines do the same thing.  Both effectively capture input
#fname = input('Enter your first name: ')
print('Enter your last name: ')
#lname = input()
#birthYear = input('When were you born? ')

#converting the string to an int
#birthYear = int(birthYear)

#eval is asking python to guess what the data type is
#evalTest = eval(birthYear)

# currentYear = 2025
# age = currentYear - birthYear

#printing integers here works fine because it is passed as an argument / parameter
#print(lname,',',fname, birthYear)
#have to convert the int to a string in order to make it part of a string
#print('Hi, my name is '+fname+' '+lname+' I am '+str(age)+' years old')

temp = 90
if temp > 86:
    #only will execute if the conditional is true
    print('Hey its hot out')
    print()
    print('hi there white space')
else:
    #only executes if the conditional is false
    print('its not that hot, maybe I\'ll go have some coffee')

print('I will check to see if it\'s raining')

# myText = input('Enter some text: ')
# shouting = ''
# #traditional approach
# #for crazyWeirdVariableName in myText:
# for c in myText:
#     if c.islower():
#         shouting += c.upper()
#     else:
#         shouting += c
# print(shouting)

lst = [1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me', ['PascalCase', 'camelCase', 'me', "Brian O'Donnell"]]
#in a range of values
for i in range(5,len(lst),1):
    print('Index is: '+str(i))
    print('item is:'+str(lst[i]))


