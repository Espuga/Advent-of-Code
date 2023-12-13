
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

def comprovar(card1, cardToPut):
    # True en cas de anar despres, False en cas de anar abans
    card1_ = sorted(dic[card1], key=lambda x: dic[card1][x], reverse=True)
    card2_ = sorted(dic[cardToPut], key=lambda x: dic[cardToPut][x], reverse=True)
    keys1 = list(card1_.keys())
    keys2 = list(card2_.keys())
    for x in range(len(list(card1_.keys()))):
        if dic[card1][keys1[x]] > dic[cardToPut][keys2[x]]:
            return True
    return False

def desempatar(results):
    finalResults = []
    """ 
    - fer diccionari, de card: {lletres: contadorLletres}
    - per cada card dins de results, recorro finalResults, i la poso on toque
    """

    for cardToPut in results:
        afegit = False
        # Per cada carta que s'ha de ordenar
        if len(finalResults) != 0:
            # Si hi han elements
            for i in range(len(finalResults)-1):
                # Per cada carta ja afegida, comprovar per saver on colocar la nova
                if comprovar(finalResults[i], cardToPut) == False:
                    finalResults.insert(i, cardToPut)
                    break
            if afegit == False:
                finalResults.append(cardToPut)
        else:
            # si no hi han elements, afegir directament
            finalResults.append(cardToPut)
    return finalResults

                

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

dic = {}

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
    dic[card] = cardSplit
    for key in list(cardSplit.keys()):
        aux.append(cardSplit[key])
    aux.sort(reverse=True)
    results[posicionar(aux)].append(card)

finalResult = 0


aux = len(list(cardsPonits.keys()))
for key in list(results.keys()):
    if len(results[key]) == 1:
        print(results[key][0])
        finalResult += int(cardsPonits[results[key][0]])*aux
        aux -= 1
    elif len(results[key]) > 1:
        desempats = desempatar(results[key])
        for desempat in desempats:
            print(desempat)
            finalResult += int(cardsPonits[desempat])*aux
            aux -= 1
print(finalResult)