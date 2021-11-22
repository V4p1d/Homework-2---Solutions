# Write a function that receives two dictionaries. The function will return
# a dictionary that contains the keywords and the values of the two dictionaries combined.
# If the dictionaries contain the same key, the function will take only the
#  value of the first dictionary.
# example: input1 = {"a": 1, "b": 2}, input2 = {"b": 1, "c": 2}, output = {"a": 1, "b": 2, "c": 2}


def combDict(dictionary1, dictionary2):

    dictionaryCombined = dictionary1

    for key, value in dictionary2.items:
        if key not in dictionary1.keys():
            dictionaryCombined[key] = value

    
    return dictionaryCombined
