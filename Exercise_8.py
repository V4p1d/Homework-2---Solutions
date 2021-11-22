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
# And the following list of student dictionaries

students = [Pietro, Andrew, Lianna]

# Write a function that takes a list of student dictionaries (any number of students) and returns the
# average marks of the students respectively for homeworks, quizzes and tests. You can use the function of exercise 7
# to make it more readable.


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



    return avgHomework, avgQuiz, avgTest

print(studentsAvgs(students))
