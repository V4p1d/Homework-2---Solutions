# Write a function that receives two inputs, a list and a dictionary.
# The function will return a list containing the common elements, between the list and 
# the keywords of the dictionary.
# Provide examples to show that the function works as intended.
# Example: list = ["cat", "1"], dictionary = {"cat": 1, 1: 15}, output = ["cat"]

def commonKeywords(list, dictionary):
    commonList = []

    for word in list:
        if word in dictionary.keys():
            commonList.append(word)

    return commonList

list = ["cat", "1"]
dictionary = {"cat": 1, 1: 15}

print(commonKeywords(list, dictionary))