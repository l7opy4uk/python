
## Geron formule
def geron_formule():
    
    a = int(input("a?"))
    b = int(input("b?"))
    c = int(input("c?"))

    p = (a + b + c)/2

    #p = int(p)

    print("p =", p)

    S = (p*(p - a)*(p - b)*(p - c))**0.5

    print("S =",S)

    print((a + b > c) and (a + c > b) and (c + b > a))

def polindrom():

    poli = input("Input your word: ")
    print(poli == poli[::-1])

polindrom()

