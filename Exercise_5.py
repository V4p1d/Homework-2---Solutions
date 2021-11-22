# Write a function that receives two lists as input. The function will return an ordered list that
# contains the elements of both input lists. Any common occurrences will be duplicated.
# Provide examples to show that the function works as intended.
# Example: list1 = [1, 1, 5, 3], list2 = [1, 3, 5, 19, 17], output = [1, 1, 1, 3, 3, 5, 5, 17, 19]

def mergeSort(list1, list2):

    notSortedList = list1 + list2
    sortedList = []
    for item in notSortedList:
        if sortedList == []:
            sortedList.append(item)
        else:
            for index, compItem in enumerate(sortedList):
            
                if item < compItem:

                    sortedList.insert(index, item)

                    break

                if index + 1  == len(sortedList):

                    sortedList.append(item)

                    break
                    


    return sortedList

list1 = [22, 32.1, 5, 12, 1, 1, 5, 3]
list2 = [1, -3, 5, 19, 17]

print(mergeSort(list1, list2))