firstNumber = "Bob"
secondNumber = "Bob 2 electric Boogaloo"
while type(firstNumber) != int:
    try:
        firstNumber = int(input("Please Type Your First Number: "))
        print(f"Cool Your First Number is {firstNumber}\n")
    except ValueError:
        print("That's not a number Silly!")
while type(secondNumber) != int:
    try:
        secondNumber = int(input("Please Type Your Second Number: "))
        print(f"Cool Your Second Number is {secondNumber}\n")
    except ValueError:
        print("That's not a number Silly!")
if firstNumber > secondNumber:
    print(f"{firstNumber} is greater than {secondNumber}")
elif firstNumber < secondNumber:
    print(f"{secondNumber} is greater than {firstNumber}")
else:
    print("Your Numbers are the exact same Silly!")
