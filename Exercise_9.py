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

# Write a function that takes the score of a student and turns that into a letter.
# If score is 70 or above: return "A"
# Else if score is 60 or above return "B"
# Else if score is 50 or above return "C"
# Else if score is 40 or above return "D"
# Otherwise return "F"


def letterScore(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

# Use the functions defined in the previous two exercises to obtain 
# the average letter score of the class, respectively for homework, quizzes and tests.


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

def studentsAvgs(students):
    avgHomework = 0
    avgQuiz = 0
    avgTest = 0
    grades = []

    for student in students:
        grades.append(getAvgs(student))

    for grade in grades:
        avgHomework += grade[0]
        avgQuiz += grade[1]
        avgTest += grade[2]

    avgHomework = avgHomework/len(grades)
    avgQuiz = avgQuiz/len(grades)
    avgTest = avgTest/len(grades)



    return letterScore(avgHomework), letterScore(avgQuiz), letterScore(avgTest)


students = [Pietro, Andrew, Lianna]

print(studentsAvgs(students))