
## Geron formule
def geron_formule():
    
    try:
        a = int(input("a?"))
        b = int(input("b?"))
        c = int(input("c?"))

        if not ((a + b > c) and (a + c > b) and (c + b > a)):
            raise ValueError("Triangle doesn't exist")
         
    except ValueError as err:
            
            print(err)
            exit()
    
    else:
        p = (a + b + c)/2
        print("p =", p)
        S = (p*(p - a)*(p - b)*(p - c))**0.5
        print("S =",S)


def polindrom():

    poli = input("Input your word: ")
    print(poli == poli[::-1])



geron_formule()


grn1 = kop50 = kop25 = kop5 = kop1 = 0.00
try:
    amount = float(input("Input amount of your money: "))
    if amount < 0:
        raise ValueError
except:
    print("Error! Wrong input.")
else:
    grn1= amount // 1
    amount = (amount % 1)*100
    kop50 = amount // 50
    amount = amount % 50
    kop25 = amount // 25
    amount = amount % 25
    kop5 = amount // 5
    amount = amount % 5
    kop1 = amount // 1

    if grn1 > 0:
        print("По 1 грн нужно: \t",  int(grn1))
    if kop50 > 0:
        print("По 50 коп нужно: \t",  int(kop50))
    if kop25 > 0:
        print("По 25 коп нужно: \t",  int(kop25))
    if kop5 > 0:
        print("По 5 коп нужно: \t",  int(kop5))
    if kop1 > 0:
        print("По 1 коп нужно: \t",  int(kop1))
    


