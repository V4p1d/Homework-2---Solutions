# Consider the following dictionaries corresponding to student's grades

Pietro = {
    "name": "Pietro",
    "homework": [90.0,97.0,75.0,92.0],
    "quizzes": [88.0,40.0,94.0],
    "tests": [75.0,90.0]
}
Andrew = {
    "name": "Andrew",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
Lianna = {
    "name": "Lianna",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Write a function that takes a student dictionary and returns three outputs.
# Respectively, their average grade in homework, quizzes and tests.
# Example: input = Pietro, output1 = 88.5, output2 = 74.0, output3 = 82.5

def getAvgs(dictionary):
    avgHomework = 0
    avgQuiz = 0
    avgTest = 0

    for element in dictionary["homework"]:
        avgHomework += element
    for element in dictionary["quizzes"]:
        avgQuiz += element
    for element in dictionary["tests"]:
        avgTest += element

    avgHomework = avgHomework/len(dictionary["homework"])
    avgQuiz = avgQuiz/len(dictionary["quizzes"])
    avgTest = avgTest/len(dictionary["tests"])
    return avgHomework, avgQuiz, avgTest

print(getAvgs(Pietro))
print(getAvgs(Andrew))
print(getAvgs(Lianna))
