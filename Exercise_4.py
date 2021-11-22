# Write a function that receives two inputs, a string and a character.
# The function will return a new string equal to the input string without 
# any occurrences of the character.
# Provide examples to show that the function works as intended.
# Example: string = "hello, I'm happy.", char = "l", output = "Heo I'm happy."

def stringSplit(string, char):

    splittedString = ""
    for letter in string:
        if letter != char:
            splittedString += letter

    return splittedString

string1 = "hello, I'm happy."
char1 = "l"

print(stringSplit(string1, char1))

string2 = "hello, I'm happy."
char2 = "p"

print(stringSplit(string2, char2))