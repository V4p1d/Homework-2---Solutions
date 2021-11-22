# Write a function that receives two strings as an input. The second input is optional 
# and by default will be equal to "odd". 
# The function will return a string, equal to the input string except, if the second input is equal to
# "odd", the elements of the string with odd indeces will be removed whereas if the second input is equal
# to "even", the elements of the string with even indeces will be removed. For this exercise, treat index 0
# as even.
# Provide examples to show that the function works as intended.
# Example: string1 = "Oblivious", string2 = "odd", output = "Olvos"
# Example: string1 = "Oblivious", string2 = "even", output = "biiu"

def removeChars(string, pos = "odd"):
    stringStripped = ""

    if pos == "odd":
        for index, letter in enumerate(string):

            if index%2 == 0:
                stringStripped += letter
    elif pos == "even":
        for index, letter in enumerate(string):

            if index%2 == 1:
                stringStripped += letter
        
    
    return stringStripped

string1 = "Oblivious"
print(removeChars(string1))
print(removeChars(string1, pos = "even"))


'''
IMPORTANT
You can access the individual elements of a string as if the string was a tuple (strings are also immutable).
For example:

    myString = "hello"

myString[0] would be equal to h, myString[1] would be equal to e and so on. 

You can also access portions of the string using slices (as in lists and tuples)

mystring[0:3] would be equal to "hel"

This means that you can also use a string in a for loop as if it was a list:

for letter in myString:
    print(letter)

This code would output every letter in the string individually.

'''