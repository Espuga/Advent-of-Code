def isMultiplicar(linies, x, y):
    # return True if linies[y][x] == "*" else False
    # print(linies[y][x])
    # print(linies[y][x] == "*")
    if linies[y][x] == "*":
        return True
    return False
def afegir2(linies, x, y):
    # print(isMultiplicar(linies, x, y))
    if isMultiplicar(linies, x, y):
        # print(str(y)+","+str(x))
        return [True, str(y)+","+str(x)]
    return [False]

def comprovar(linies, x, y):
    global multiplicar, posicio
    # Per sobre
    if y-1 >= 0:    # si hi pot haver numeros per sobre
        if x-1 >= 0:      # si hi pot haver numeros per sobre - radere
            if linies[y-1][x-1] != "." and linies[y-1][x-1].isdigit() == False:     # Si hi ha un caracter especial -1 -1
                a = afegir2(linies, x-1, y-1)
                multiplicar = a[0]
                posicio = a[1] if a[0] else ""
                return True
        if linies[y-1][x] != "." and linies[y-1][x].isdigit() == False:     # Si hi ha un caracter especial -1 0
            a = afegir2(linies, x, y-1)
            multiplicar = a[0]
            posicio = a[1] if a[0] else ""
            return True
        if x+1 < len(linies[y]):      # si hi pot haver numeros per sobre - radere
            if linies[y-1][x+1] != "." and linies[y-1][x+1].isdigit() == False:     # Si hi ha un caracter especial -1 +1
                a = afegir2(linies, x+1, y-1)
                multiplicar = a[0]
                posicio = a[1] if a[0] else ""
                return True
    # Mateix nivell
    if x-1 >= 0:      # si hi pot haver numeros per sobre - radere
        if linies[y][x-1] != "." and linies[y][x-1].isdigit() == False:     # Si hi ha un caracter especial 0 -1
            a = afegir2(linies, x-1, y)
            multiplicar = a[0]
            posicio = a[1] if a[0] else ""
            return True
    if x+1 < len(linies[y]):      # si hi pot haver numeros per sobre - radere
        if linies[y][x+1] != "." and linies[y][x+1].isdigit() == False:     # Si hi ha un caracter especial 0 +1
            a = afegir2(linies, x+1, y)
            multiplicar = a[0]
            posicio = a[1] if a[0] else ""
            return True
    # Per sota
    if y+1 < len(linies):    # si hi pot haver numeros per sobre
        if x-1 >= 0:      # si hi pot haver numeros per sobre - radere
            if linies[y+1][x-1] != "." and linies[y+1][x-1].isdigit() == False:     # Si hi ha un caracter especial +1 -1
                a = afegir2(linies, x-1, y+1)
                multiplicar = a[0]
                posicio = a[1] if a[0] else ""
                return True
        if linies[y+1][x] != "." and linies[y+1][x].isdigit() == False:     # Si hi ha un caracter especial +1 0
            a = afegir2(linies, x, y+1)
            multiplicar = a[0]
            posicio = a[1] if a[0] else ""
            return True
        if x+1 < len(linies[y]):      # si hi pot haver numeros per sobre - radere
            if linies[y+1][x+1] != "." and linies[y+1][x+1].isdigit() == False:     # Si hi ha un caracter especial +1 +1
                a = afegir2(linies, x+1, y+1)
                multiplicar = a[0]
                posicio = a[1] if a[0] else ""
                return True
    return False


with open("./inputs/input3.txt", "r") as f:
    linies = []
    linies2 = f.readlines()

    for linia in linies2:
        linies.append(linia.strip())

    result = 0
    result2 = 0
    diccionari = {}

    y = 0
    while y < len(linies):
        x = 0
        #if y == 38: print(linies[y])
        current = False
        currentNumber = ""
        multiplicar = False
        posicio = ""

        while x < len(linies[y]):
            # print(linies[y][x])

            if linies[y][x].isdigit():  # si es un numero
                currentNumber += linies[y][x]
                if current == False:
                    current = comprovar(linies, x, y)
            else:
                if current and currentNumber != "":
                    if y == 3: print(currentNumber)
                    result += int(currentNumber)
                    #print(multiplicar)
                    if multiplicar:
                        try:
                            diccionari[posicio].append(int(currentNumber)) 
                        except:
                            diccionari[posicio] = [int(currentNumber)] 
                        multiplicar = False
                currentNumber = ""
                current = False

            x += 1
        if current and currentNumber != "":
            #if y == 3: print(currentNumber)
            result += int(currentNumber)
            if multiplicar:
                try:
                    diccionari[posicio].append(int(currentNumber)) 
                except:
                    diccionari[posicio] = [int(currentNumber)] 
                multiplicar = False
        currentNumber = ""
        current = False

        y += 1
    print(diccionari)
    for key in list(diccionari.keys()):
        if len(diccionari[key]) > 1:
            aux = 1
            for c1 in diccionari[key]:
                aux *= c1
            result2 += aux

    print(result2)