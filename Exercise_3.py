# Write a function that receives a dictionary and returns the same dictionary but 
# with inverted keywords and elements
# Provide examples to show that the function works as intended.
# Example: input = {1: "cat", 5: "dog"}, output = {"cat": 1, "dog": 5}


def invertDictionary(dictionary):

    invertedDictionary = {j:i for i,j in dictionary.items()}


    return invertedDictionary


input = {1: "cat", 5: "dog"}

print(invertDictionary(input))