def getFirst(linia, diccionari):
    i = 0
    while i < len(linia):
        if linia[i].isdigit():
            return linia[i]
        else:
            for num in list(diccionari.keys()):
                aux = 0
                moment = True
                while aux < len(num):
                    if num[aux] != linia[i+aux]:
                        moment = False
                        break
                    aux += 1
                if moment:
                    return diccionari[num]
        i += 1


def getLast(linia, diccionari):
    i = len(linia)-1
    while i >= 0:
        if linia[i].isdigit():
            return linia[i]
        else:
            for num in list(diccionari.keys()):
                aux = len(num)-1
                aux2 = 0
                moment = True
                while aux >= 0:
                    if num[aux] != linia[i-aux2]:
                        moment = False
                        break
                    aux -= 1
                    aux2 += 1
                if moment:
                    return diccionari[num]
        i -= 1

diccionari = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("./inputs/input1.txt", "r") as f:
    linies = f.readlines()

    resultat = 0

    for linia in linies:
        # print(getFirst(linia, diccionari))
        # print(getLast(linia, diccionari))
        # print(str(getFirst(linia, diccionari))+str(getLast(linia, diccionari)))
        resultat += int(str(getFirst(linia, diccionari))+str(getLast(linia, diccionari)))
    print(resultat)