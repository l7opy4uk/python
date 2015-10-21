def fileWriting(dataList):
    fileExt = 0
    fileName = " "
    fileNameFull = " "
    WRITE = "w"
    print("Please enter your file name")
    fileName = input()
    print("Choose extension for your file\n 1.txt\n 2.csv")
    fileExt = int(input("Please enter the digit: "))
    while fileExt != 1 and fileExt != 2:
        fileExt = input("Please, choose ext. from the list and enter the digit:")
    if fileExt == 1:
        fileNameFull = fileName + ".txt"
    elif fileExt == 2:
        fileNameFull = fileName + ".csv"
    print("File will be saved as " + fileNameFull)
    with open(fileNameFull, mode = WRITE) as fileToWrite:
        for data in dataList:
            fileToWrite.write(data)
    fileToWrite.close()
    return

#Для сбора информации от пользователя.
#For input data from user.
def dataInput():
    data = " "
    dataList = [ ]
    dataListSepar = [ ]
    print("Please enter your data (when you will finish, write DONE):")
    while data != "DONE":
            data = input()
            dataList.append("\n" + data)
    dataList.remove("\nDONE")
##  Печатает список в нормально виде.
##  dataListSepar = "\n".join(dataList)
##    print(dataListSepar)
    return dataList

dataList = dataInput()
fileWriting(dataList)
