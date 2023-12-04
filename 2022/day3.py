f = open('entrades/day3_entrades.txt', 'r')
linies = f.readlines()

diccionari = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
    'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,  'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 
    'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 
    'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47,  'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52, 
}


#   Part 1
punts = 0
for linia in linies:
    meitat1 = ""
    meitat2 = ""
    primer = True
    llargada = int(len(linia))
    meitat = int(len(linia)/2)
    index = 0
    while index < llargada:
        if index >= meitat:
            primer = False
        if primer:
            meitat1 = meitat1 + linia[index]
        else:
            meitat2 = meitat2 + linia[index]
        index += 1
    guardades = []
    guardat = False
    for c1 in meitat1:
        for c2 in guardades:
            if c1 == c2:
                guardat = True
        if guardat == False:
            contador = meitat2.count(c1)
            if contador != 0:
                guardades.append(c1)
                punts += diccionari[c1]
print(punts)


print("Part 2")
# Part 2
linea1 = ""
linea2 = ""
liena3 = ""
contador_linea = 1
punts = 0
for linia in linies:
    if contador_linea == 1:
        linea1 = linia
        contador_linea += 1
    elif contador_linea == 2:
        linea2 = linia
        contador_linea += 1
    elif contador_linea == 3:
        linea3 = linia
        contador_linea = 1
        
        for c3 in linea1:
            contador2 = linea2.count(c3)
            contador3 = linea3.count(c3)
            if contador2 != 0 and contador3 != 0:
                punts += diccionari[c3]
                break
print(punts)