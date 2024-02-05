from random import randint
dom = [randint(0,5) for x in range(42)]
domlar = []
for x in range(66):
    domlar.append([randint(0,5) for x in range(42)])
print(domlar)
"""
summa = []
def tekshir(a):
    s = 8000
    match a:
        case 0:
            natija = 0
        case 1:
            natija = s
        case 2:
            natija = s+s*0.25
        case 3:
            natija = s+s*0.25+s*0.15
        case 4:
            natija = s+s*0.25+s*0.15+s*0.1
        case 5:
            natija = s+s*0.25+s*0.15+s*0.1+s*0.05
    return(natija)
sch=0
for i in dom:
    sch+=1
    summa.append(tekshir(i))
    print(sch,"-",tekshir(i)," so'm")
print(summa)

"""

