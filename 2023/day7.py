
def posicionar(llista):
    if llista[0] == 5:
        return 6
    elif llista[0] == 4 and llista[1] == 1:
        return 5
    elif llista[0] == 3 and llista[1] == 2:
        return 4
    elif llista[0] == 3 and llista[1] == 1 and llista[2] == 1:
        return 3    
    elif llista[0] == 2 and llista[1] == 2 and llista[2] == 1:
        return 2
    elif llista[0] == 2 and llista[1] == 1 and llista[2] == 1 and llista[3] == 1:
        return 1
    return 0

def mesGran(carta, c1):
    aux = 0
    for caracter in carta:
        if carta.count(caracter) > aux:
            aux = carta.count(caracter)
    if carta.count(c1) == aux:
        return True
    return False

def desempatar(results):
    # card: valor
    # retornar una llista amb les cartes ordenades

    # numero de repeitcions més gran de la carta, i guardar la lletra 
    """lletres2 = []
    for card in results:
        aux = 0
        car = ""
        for caracter in card:
            if card.count(caracter) > aux:
                aux = card.count(caracter)
                car = caracter
        lletres2.append(car)
    puntsLletres = {}
    for lletra in lletres2:
        puntsLletres[lletra] = lletres[lletra]
    ordenat = sorted(puntsLletres, key=lambda x: puntsLletres[x], reverse=True)
    result2 = [] #cartes ordenades finals
    for c1 in ordenat: 
        for carta in results:
            if mesGran(carta, c1):
                result2.append(carta)
    return result2"""

    """ 
    diccionari de carta: lletra per desempatar
    """
    a = {
        "A": [],
        "K": [],
        "Q": [],
        "J": [],
        "T": [],
        "9": [],
        "8": [],
        "7": [],
        "6": [],
        "5": [],
        "4": [],
        "3": [],
        "2": [],
    }
    for carta in results:
        for keyLletra in list(diccionari[carta].keys()):
            if mesGran(carta, diccionari[carta][keyLletra]):
                

linies = open("./inputs/prova7.txt", "r").readlines()

lletres = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

results = {
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: [],
    0: []
}

cardsPonits = {}

diccionari = {}

for linia in linies:
    card, points = linia.strip().split()
    cardsPonits[card] = points
    cardSplit = {}
    for caracter in card:
        try:
            cardSplit[caracter] += 1
        except:
            cardSplit[caracter] = 1
    aux = []
    diccionari[card] = cardSplit
    for key in list(cardSplit.keys()):
        aux.append(cardSplit[key])
    aux.sort(reverse=True)
    results[posicionar(aux)].append(card)

finalResult = 0


aux = len(list(cardsPonits.keys()))
for key in list(results.keys()):
    if len(results[key]) == 1:
        #print(results[key][0])
        finalResult += int(cardsPonits[results[key][0]])*aux
        aux -= 1
    elif len(results[key]) > 1:
        desempats = desempatar(results[key])
        for desempat in desempats:
            #print(desempat)
            finalResult += int(cardsPonits[desempat])*aux
            aux -= 1
print(finalResult)