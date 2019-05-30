import random


def main():
    # declare variables
    counter = 0
    studentName = "NO NAME"
    averageRight = 0.0
    right = 0.0
    number1 = 0
    number2 = 0
    answer = 0.0
    
    studentName = getName()

    while counter < 10:
        # initialize variables
        number1, number2 = getNumbers()
        answer = getAnswer(number1, number2)  # answer removed as argument
        right = checkAnswer(number1, number2, answer, right)
        counter = counter + 1

        # end of while loop

        averageRight = results(right) # averageRight removed as argument
        displayInfo(right, averageRight, studentName)


# this function gets the players names
def getName():
    studentName = input("Enter students name: ")
    return studentName


def getNumbers():  # getNumbers with no parameters
    number1 = random.randint(1, 500)
    number2 = random.randint(1, 500)
    return number1, number2


# getAnswer
def getAnswer(number1, number2): # answer removed as parameter 
    print("What is the answer to the following equation?: ")
    print(number1)
    print("+")
    print(number2)
    answer = int(input("What is the sum?: "))
    return answer


# checkAnswer
def checkAnswer(number1, number2, answer, right):
    if answer == number1 + number2:
        print("Right")
        right = right + 1
    else:
        print("Wrong")

    return right


# function getAverage
def results(right): # averageRight removed as parameter 
    averageRight = float(right) / 10
    return averageRight


# print average
def displayInfo(right, averageRight, studentName):
    print("Information for student: ", studentName)
    print("The number right is: ", right)
    print("The average right is: ", averageRight)


main()
