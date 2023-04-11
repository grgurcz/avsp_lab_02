import sys
import math
import time


def PCY(br_kosara, s, br_pretinaca, kosare):
    prag = math.floor(s * br_kosara)

    br_predmeta = {}

    for kosara in kosare:
        for predmet in kosara:
            if predmet not in br_predmeta:
                br_predmeta[predmet] = 0
            br_predmeta[predmet] += 1
    
    A = 0
    for predmet in br_predmeta:
        if br_predmeta[predmet] >= prag:
            A += 1
    
    A = A * (A - 1) // 2

    pretinci = {}

    for kosara in kosare:
        for i in range(len(kosara)):
            for j in range(i + 1, len(kosara)):
                predmet1 = kosara[i]
                predmet2 = kosara[j]
                if br_predmeta[predmet1] >= prag and br_predmeta[predmet2] >= prag:
                    k = (i * len(br_predmeta) + j) % br_pretinaca
                    if k not in pretinci:
                        pretinci[k] = 0
                    pretinci[k] += 1

    parovi = {}

    for kosara in kosare:
        for i in range(len(kosara)):
            for j in range(i + 1, len(kosara)):
                predmet1 = kosara[i]
                predmet2 = kosara[j]
                if br_predmeta[predmet1] >= prag and br_predmeta[predmet2] >= prag:
                    k = (i * len(br_predmeta) + j) % br_pretinaca
                    if pretinci[k] >= prag:
                        if not (predmet1, predmet2) in parovi:
                            parovi[(predmet1, predmet2)] = 0
                        parovi[(predmet1, predmet2)] += 1

    print(A)

    P = 0
    
    for x in reversed(sorted(parovi.values())):
        if x < prag:
            break
        P += 1
    
    print(P)

    for x in reversed(sorted(parovi.values())):
        if x < prag:
            break
        print(x)
    

def main():
    br_kosara = int(sys.stdin.readline())
    s = float(sys.stdin.readline())
    br_pretinaca = int(sys.stdin.readline())
    kosare = []
    for i in range(br_kosara):
        kosara  = [int(broj) for broj in sys.stdin.readline().strip().split()]
        kosare.append(kosara)
    
    PCY(br_kosara, s, br_pretinaca, kosare)



if __name__=='__main__':
    time1 = time.time()
    main()
    time2 = time.time()
    print(time2 - time1)