studentList = ["Bob", "Ethan", "Hunter"]
scoreList = [80, 10, 60]


def gradeAllocator(score):
    if score >= 90:
        return "A+"
    elif score >= 85:
        return "A"
    elif score >= 80:
        return "A-"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "B-"
    elif score >= 60:
        return "C+"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "C-"
    elif score >= 40:
        return "D"
    elif score >= 0:
        return "E"


def studentScoreGetter9000():
    studentName = input("What is the student's name (type x to stop): "
                        "").capitalize()
    if studentName == "X":
        while len(studentList) > 0:
            print(studentList.pop(), gradeAllocator(scoreList.pop()))
        else:
            quit()
    else:
        studentScore = input(f"What score did {studentName} get? (0-100): ")
    studentList.append(studentName)
    scoreList.append(studentScore)


while True:
    studentScoreGetter9000()


