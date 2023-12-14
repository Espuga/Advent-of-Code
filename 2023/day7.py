import sys

class SortFile:
  def __init__(self, file_path):
    self.lines = open(file_path, "r").readlines()
    self.lletres = {
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
    self.results = {
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: [],
        0: []
    }
    self.cardsPonits = {}
    self.dic = {}
  
  def sortCards(self):
    a = 0
    for linia in self.lines:
      a += 1
      card, points = linia.strip().split()
      self.classificarCards(card, points)
    print(a)
    return self.countPoints()

  def classificarCards(self, card, points):
    self.cardsPonits[card] = points
    cardSplit = {}
    for caracter in card:
        try:
            cardSplit[caracter] += 1
        except:
            cardSplit[caracter] = 1
    aux = []
    self.dic[card] = cardSplit
    for key in list(cardSplit.keys()):
        aux.append(cardSplit[key])
    aux.sort(reverse=True)
    self.results[self.posicionar(aux)].append(card)
  
  def countPoints(self):
    finalResult = 0
    aux = len(list(self.cardsPonits.keys()))
    for key in list(self.results.keys()):
        print("=============")
        if len(self.results[key]) == 1:
            print(self.results[key][0])
            finalResult += int(self.cardsPonits[self.results[key][0]])*aux
            aux -= 1
        elif len(self.results[key]) > 1:
            desempats = self.sortClassifiedCards(self.results[key])
            for desempat in desempats:
                print(desempat)
                finalResult += int(self.cardsPonits[desempat])*aux
                aux -= 1
    return finalResult

  def sortClassifiedCards(self, results):
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
            for i in range(len(finalResults)):
                # Per cada carta ja afegida, comprovar per saver on colocar la nova
                if self.comprovar(finalResults[i], cardToPut) == False:
                    finalResults.insert(i, cardToPut)
                    afegit = True
                    break
            if afegit == False:
                finalResults.append(cardToPut)
        else:
            # si no hi han elements, afegir directament
            finalResults.append(cardToPut)
    return finalResults


  def comprovar(self, card1, cardToPut):
    # True en cas de anar despres, False en cas de anar abans
    keys1 = sorted(self.dic[card1], key=lambda x: self.dic[card1][x], reverse=True)
    keys2 = sorted(self.dic[cardToPut], key=lambda x: self.dic[cardToPut][x], reverse=True)
    for x in range(len(keys1)):
      #print(dic[card1][keys1[x]])
      k1 = self.lletres[keys1[x]]
      k2 = self.lletres[keys2[x]]
      if k1 < k2:
          return False
      elif k1 > k2: 
        return True
    return True
  
  def posicionar(self, llista):
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        #print("Example: python3 day7.py <file_path>")
        file_processor = SortFile("./inputs/input7.txt")
        result = file_processor.sortCards()
        print(result)
    else:
        file_path = sys.argv[1]
        file_processor = SortFile(file_path)
        result = file_processor.sortCards()
        print(result)
    
    
