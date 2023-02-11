def numberChecker():
    numList = []
    firstNum = int(input("GIVE FIRST NUMBER OF LIST: "))
    finalNum = int(input("GIVE FINAL NUMBER OF LIST: "))
    if firstNum == finalNum:
        numList.append(firstNum)
        return 0
    while firstNum > finalNum:
        print("Your First Number is greater than the last number Silly!")
        firstNum = int(input("GIVE FIRST NUMBER OF LIST: "))
        finalNum = int(input("GIVE FINAL NUMBER OF LIST: "))
    numList.append(firstNum)
    while firstNum + 1 < finalNum:
        firstNum = firstNum + 1
        numList.append(firstNum)
    numList.append(finalNum)
    return f"{numList} And a total of {sum(numList)}"


print(numberChecker())
