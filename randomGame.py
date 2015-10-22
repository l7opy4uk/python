## Тестировал функцию .replace()
import random
def test():
    print("Хочешь дружить? \
    \n1. Yes\
    \n2. No")
    inputFriend = " "
    inputFriend = input()
    while inputFriend != "1" and inputFriend !="2":
        inputFriend = input("Ты криворукий что ли? Вводи еще раз. ")
    if inputFriend =="1":
        print("Красава!")
    else:
        print("Ну и нахуй пошел!")
        messageWhere = "Ну а если не нахуй, то куда? Свой вариант давай: "
        print(messageWhere)
        inputWhere = input()
        while inputWhere.lower() != "нахуй":
            print(messageWhere.replace("нахуй", inputWhere))
            inputWhere = input()
        else:
            print("А ты ерепенился =)")

            
## Пробовал написать функцию, которая будет просто брать инпут,
## но почему-то она не возвращает значение. Пишет что inputNumber - not defind.
def inputNumberFun():
        inputNumberStr = input("Enter your number: ")
        inputNumber = int(inputNumberStr)
        return inputNumber


## Игра по угадыванию чисел из ряда от 0 до 100.
def randomNumberGame():
    print("You need to guess a number in range from 0 to 100."\
          "\nYou will have a hint every time")
    randomNumber = random.randint(1,100)
    strLess = "It's less..."
    strMore = "It's more"
    inputNumberStr = inputEmptyCheck("Enter your number: ")
    inputNumber = int(inputNumberStr)
    count = 0
    while randomNumber != inputNumber:
        if randomNumber < inputNumber:
            print(strLess)
            inputNumberStr = inputEmptyCheck("Enter your number: ")
            inputNumber = int(inputNumberStr)
            count += 1
        elif randomNumber > inputNumber:
            print(strMore)
            inputNumberStr = inputEmptyCheck("Enter your number: ")
            inputNumber = int(inputNumberStr)
            count += 1
    print("Bingo, it takes you " + str(count) + " attempts to guess a number")




## Will check for empty field. Usage example:
##inputName = (inputEmptyCheck("Login: ")
def inputEmptyCheck(inputMessage):
    varName = ""
    while not varName:
        varName = input(inputMessage)
    return varName


randomNumberGame()
    
