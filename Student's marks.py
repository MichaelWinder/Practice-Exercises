studentList = []
scoreList = []


def studentScoreGetter9000():
    studentName = input("What is the student's name (type x to stop): "
                        "").capitalize()
    if studentName == "X":
        listIndex = scoreList.index(max(scoreList))
        print(f"The student with the highest score was "
              f"{studentList[listIndex]} with a score of {max(scoreList)}.\n"
              f"Also the average score was {sum(scoreList) / len(scoreList)}")
        quit("YOU HAVE GREAT STUDENTS! :)))")
    else:
        studentScore = int(input(f"What score did {studentName} get? ("
                                 f"0-100): "))
    studentList.append(studentName)
    scoreList.append(studentScore)


while True:
    studentScoreGetter9000()
