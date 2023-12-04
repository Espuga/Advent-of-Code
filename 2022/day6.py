f = open('entrades/day6_entrades.txt', 'r')
linies = f.read()

#   Part 1
""" primer = ""
segon = ""
tercer = ""
cuart = ""
contador = 0
for c1 in linies:
    cuart = tercer
    tercer = segon
    segon = primer
    primer = c1
    if cuart != "":
        if cuart != tercer and cuart != segon and cuart != primer and tercer != segon and tercer != primer and segon != primer:
            print(contador+4)
            break
        else:
            contador += 1 """

#   Part 2
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
a10 = ""
a11 = ""
a12 = ""
a13 = ""
a14 = ""
contador = 14
for c1 in linies:
    a14 = a13
    a13 = a12
    a12 = a11
    a11 = a10
    a10 = a9
    a9 = a8
    a8 = a7
    a7 = a6
    a6 = a5
    a5 = a4
    a4 = a3
    a3 = a2
    a2 = a1
    a1 = c1
    if a14 != "":
        if a14 != a13 and a14 != a12 and a14 != a11 and a14 != a10 and a14 != a9 and a14 != a8 and a14 != a7 and a14 != a6 and a14 != a5 and a14 != a4 and a14 != a3 and a14 != a2 and a14 != a11:
            if a13 != a12 and a13 != a11 and a13 != a10 and a13 != a9 and a13 != a8 and a13 != a7 and a13 != a6 and a13 != a5 and a13 != a4 and a13 != a3 and a13 != a2 and a13 != a1:
                if a12 != a11 and a12 != a10 and a12 != a9 and a12 != a8 and a12 != a7 and a12 != a6 and a12 != a5 and a12 != a4 and a12 != a3 and a12 != a2 and a12 != a1:
                    if a11 != a10 and a11 != a9 and a11 != a8 and a11 != a7 and a11 != a6 and a11 != a5 and a11 != a4 and a11 != a3 and a11 != a2 and a11 != a1:
                        if a10 != a9 and a10 != a8 and a10 != a7 and a10 != a6 and a10 != a5 and a10 != a4 and a10 != a3 and a10 != a2 and a10 != a1:
                            if a9 != a8 and a9 != a7 and a9 != a6 and a9 != a5 and a9 != a4 and a9 != a3 and a9 != a2 and a9 != a1: 
                                if a8 != a7 and a8 != a6 and a8 != a5 and a8 != a4 and a8 != a3 and a8 != a2 and a8 != a1:
                                    if a7 != a6 and a7 != a5 and a7 != a4 and a7 != a3 and a7 != a2 and a7 != a1:
                                        if a6 != a5 and a6 != a4 and a6 != a3 and a6 != a2 and a6 != a1:
                                            if a5 != a4 and a5 != a3 and a5 != a2 and a5 != a1:
                                                if a4 != a3 and a4 != a2 and a4 != a1:
                                                    if a3 != a2 and a3 != a1:
                                                        if a2 != a1:
                                                            print(contador)
                                                            break
                                                        else: 
                                                            contador += 1
                                                    else:
                                                        contador += 1
                                                else:
                                                    contador += 1
                                            else:
                                                contador += 1
                                        else:
                                            contador += 1
                                    else:
                                        contador += 1
                                else:
                                    contador += 1
                            else:
                                contador += 1
                        else:
                            contador += 1
                    else:
                        contador += 1
                else:
                    contador += 1
            else:
                contador += 1 
        else:
            contador += 1

    















""" llista = []
contador = 0
bb = True
no = False
new = []
for c1 in linies:
    if bb:
        if contador < 14:
            llista.append(c1)
            contador += 1
        else:
            print(llista)
            contador += 1
            llista.append(c1)
            llista.pop(0)
            for c2 in llista:
                aa = llista.count(c2)
                if aa != 1:
                    new.append("a")
                    break
            co = new.count("a")
            if co == len(new):
                print(contador)
                break """