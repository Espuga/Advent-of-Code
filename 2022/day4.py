f = open('entrades/day4_entrades.txt', 'r')
linies = f.readlines()
contador = 0
for linia in linies:
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    current = ""
    primer = True
    for c1 in linia:
        if c1 != "-" and c1 != ",":
            current = current + c1
        else:
            if c1 == "-":
                if primer:
                    a1 = int(current)
                    current = ""
                else:
                    b1 = int(current)
                    current = ""
            elif c1 == ",": 
                a2 = int(current)
                current = ""
                primer = False
    b2 = int(current)
    
    if ((a2 < b1) | (b2 < a1)):
        pass
    else:
        contador += 1
        print(linia)
print(contador)
