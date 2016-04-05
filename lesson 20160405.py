
## Geron formule
def geron_formule():
    
    try:
        a = int(input("a?"))
        b = int(input("b?"))
        c = int(input("c?"))

        if not ((a + b > c) and (a + c > b) and (c + b > a)):
            raise ValueError
         
    except:
            print("Triangle doesn't exist")
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
