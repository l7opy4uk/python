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
        print("Ну и нафиг пошел!")
        messageWhere = "Ну а если не нафиг, то куда? Свой вариант давай: "
        print(messageWhere)
        inputWhere = input()
        while inputWhere.lower() != "нафиг":
            print(messageWhere.replace("нафиг", inputWhere))
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
    print("\tWelcome to game \"Guess the Number\"")
    print("\nYou need to guess a number in range from 0 to 100."\
          "\nThere will be a hint after every try."\
          "\nTry to do than in min. number of attempts.")
    randomNumber = random.randint(1,100)
    strLess = "It's less..."
    strMore = "It's more"
    inputNumberStr = inputEmptyDigitCheck("Enter your number: ")
    inputNumber = int(inputNumberStr)
    tries = 1
    while randomNumber != inputNumber:
        if randomNumber < inputNumber:
            print(strLess)
        else:
            print(strMore)
        inputNumberStr = inputEmptyDigitCheck("Enter your number: ")
        inputNumber = int(inputNumberStr)
        tries += 1
    print("Bingo, it's really number", randomNumber)
    print("It takes you", tries, "attempts to guess a number")
    input("\n\nPress Enter to quit.")



## Will check for empty field. Usage example:
##inputName = (inputEmptyCheck("Login: ")
def inputEmptyCheck(inputMessage):
    varName = ""
    while not varName:
        varName = input(inputMessage)
    return varName

## Will check for empty field and digits. Usage example:
##inputName = (inputEmptyDigitCheck("Login: ")
def inputEmptyDigitCheck(inputMessage):
    varName = ""
    varName = input(inputMessage)
    while not varName.isdigit():
            varName = input("(Use digits) " + inputMessage)
    return varName


##                       Coin throw game
def coingGame():
    print("\t\tWelcome to \"Coin Throwing Game\"")
    print("\nCoing will be throw 100 times, and will say result in the end."\
          "\nPress any key to start.")
    input()
    heads = 0
    tails = 0
    attemptNumber = 0
    for attemptNumber in range(100):
        coing = random.randint(1,100)
        if coing <= 50:
          heads += 1
        else:
          tails += 1
        attemptNumber += 1
    print("\n\tAvarage results:"\
          "\n\nHeads = ", heads)
    print("\nTails = ", tails)
    input("\nPress Enter to quit.")

#Игра, вы задаете число от 1 до 100, компьютер начинает отгадывать,
#Вы подсказываете ему, больше или меньше.

def SearchRandomGame():
    inputUser = int(inputEmptyDigitCheck("Enter your choosen number: "))
    while inputUser > 100:
        inputUser = int(inputEmptyDigitCheck("Enter your choosen number: "))
    rangeRandomLower = 1
    rangeRandomUpper = 100
    tries = 1
    attempt = random.randint(rangeRandomLower, rangeRandomUpper)
    while attempt != inputUser:
        print("\n=============================================================="\
              "\n\nIt's more or less then", attempt,"?")
        print("1. less"\
              "\n2. more")
        humanAnswer = inputEmptyDigitCheck("\nPlease enter the number 1 or 2: ")
        
        if inputUser < attempt:
            while int(humanAnswer) == 2:
                print("\n=============================================================="\
                      "\n\nMessage from Programmer: Please don't lie to my programm"\
                      "\n                         I watching you...")
                print("1. less"\
                      "\n2. more")
                humanAnswer = inputEmptyDigitCheck("\nPlease enter the number 1 or 2: ")
                
            if int(humanAnswer) == 1:
                rangeRandomUpper = attempt - 1
        
        elif inputUser > attempt:
            while int(humanAnswer) == 1:
                print("\n=============================================================="\
                      "\n\nMessage from Programmer: Please don't lie to my programm"\
                      "\n                         I watching you...")
                print("1. less"\
                      "\n2. more"\
                      "\n==============================================================")
                humanAnswer = inputEmptyDigitCheck("\nPlease enter the number 1 or 2: ")
                
            if int(humanAnswer) == 2:
                rangeRandomLower = attempt + 1
        else:
            humanAnswer = inputEmptyDigitCheck("Please enter the number 1 or 2: ")
        attempt = random.randint(rangeRandomLower, rangeRandomUpper)
        tries += 1
    print("\n Your number is", attempt)
    print("\n It tooks", tries, "tries from me to guess.")     
        


SearchRandomGame()     
        
          

