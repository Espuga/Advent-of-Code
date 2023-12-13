def comprovar(card1, cardToPut):
    # True en cas de anar despres, False en cas de anar abans
    keys1 = sorted(dic[card1], key=lambda x: dic[card1][x], reverse=True)
    keys2 = sorted(dic[cardToPut], key=lambda x: dic[cardToPut][x], reverse=True)
    for x in range(len(keys1)):
        if lletres[keys1[x]] > lletres[keys2[x]]:
            return True
    return False

def desempatar(results):
    finalResults = []

    for cardToPut in results:
        afegit = False
        # Per cada carta que s'ha de ordenar
        if len(finalResults) != 0:
            # Si hi han elements
            for i in range(len(finalResults)):
                # Per cada carta ja afegida, comprovar per saver on colocar la nova
                if comprovar(finalResults[i], cardToPut) == False:
                    finalResults.insert(i, cardToPut)
                    afegit = True
                    break
            if afegit == False:
                finalResults.append(cardToPut)
        else:
            # si no hi han elements, afegir directament
            finalResults.append(cardToPut)
    return finalResults

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
dic = {}
cartes = ["AAAAJ", "AAAAQ", "QQQQK"]

for card in cartes:
    cardSplit = {}
    for caracter in card:
        try:
            cardSplit[caracter] += 1
        except:
            cardSplit[caracter] = 1
    aux = []
    dic[card] = cardSplit

print(desempatar(cartes))