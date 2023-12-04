#   =====   Part 1  =====
'''
f = open('entrades/day8_entrades.txt', 'r')
linies = f.readlines()

list = []
arbres_visibles = 0

for linia in linies:
    linia = linia.strip()
    provisional_list = []
    for numero in linia:
        provisional_list.append(numero)
    list.append(provisional_list)
#   --  mostrar llista  --
""" for c1 in list:
    print(c1) """

arbres_volant = ((len(list)*2) + (len(list[0])*2)) - 4
arbres_visibles += arbres_volant
#print(arbres_volant)

index = 1
while index < len(list)-1:
    llargada = len(list[index])-1
    primer = True
    index2 = 0
    #print(list[index])
    while index2 < len(list[index]):
        if index2 == llargada:
            break
        elif primer == False:
            #print(index2)
            alçada = list[index][index2]
            visible = False

            #   ==  Esquerra    ==
            index_provisional = 0
            si = False
            #print(alçada)
            gran = []
            while index_provisional < index2:
                previous = list[index][index_provisional]
                if previous >= alçada:
                    gran.append("petit")
                else:
                    gran.append("gran")
                index_provisional += 1
            if gran.count("gran") == len(gran):
                visible = True
            
            #   ==  Dreta   ==
            index_provisional = len(list[index])-1
            si = False
            gran = []
            while index_provisional > index2:
                previous = list[index][index_provisional]
                if previous >= alçada:
                    gran.append("petit")
                else:
                    gran.append("gran")
                index_provisional -= 1
            if gran.count("gran") == len(gran):
                visible = True
                """ print(list[index])
                print(list[index][index2])
                print("visible") """

            #   ==  Top ==
            index_provisional = 0
            index_total = index
            gran = []
            while index_provisional < index_total:
                previous = list[index_provisional][index2]
                #print(previous)
                if previous >= alçada:
                    gran.append("petit")
                else:
                    gran.append("gran")
                index_provisional += 1
            if gran.count("gran") == len(gran):
                visible = True

            #   ==  Bottom  ==
            index_provisional = len(list)-1
            index_total = index
            gran = []
            while index_provisional > index_total:
                previous = list[index_provisional][index2]
                #print(previous)
                if previous >= alçada:
                    gran.append("petit")
                else:
                    gran.append("gran")
                index_provisional -= 1
            if gran.count("gran") == len(gran):
                visible = True


            if visible == True:
                arbres_visibles += 1
        else:
            primer = False
        index2 += 1
    index += 1
print(arbres_visibles)
'''



#   =====   Part 2  =====
f = open('entrades/day8_entrades.txt', 'r')
linies = f.readlines()

list = []
arbres_visibles = 0
perfecte = 0

for linia in linies:
    linia = linia.strip()
    provisional_list = []
    for numero in linia:
        provisional_list.append(numero)
    list.append(provisional_list)
#   --  mostrar llista  --
""" for c1 in list:
    print(c1) """

arbres_volant = ((len(list)*2) + (len(list[0])*2)) - 4
arbres_visibles += arbres_volant
#print(arbres_volant)


index = 1
while index < len(list)-1:
    llargada = len(list[index])-1
    primer = True
    index2 = 0
    #print(list[index])
    while index2 < len(list[index]):
        if index2 == llargada:
            break
        elif primer == False:
            #print(index2)
            alçada = list[index][index2]
            visible = False
            esquerra = 0
            dreta = 0
            top = 0
            bottom = 0

            #   ==  Esquerra    ==
            index_provisional = index2 - 1 
            si = False
            #print(alçada)
            gran = []
            while index_provisional >= 0:
                esquerra += 1
                previous = list[index][index_provisional]
                print("previous esquerra", previous)
                if previous >= alçada:
                    gran.append("petit")
                    break
                else:
                    gran.append("gran")
                index_provisional -= 1
            if gran.count("gran") == len(gran):
                visible = True
            
            
            
            #   ==  Dreta   ==
            index_provisional = index2 +1 
            si = False
            gran = []
            while index_provisional < len(list[index]):
                dreta += 1
                previous = list[index][index_provisional]
                print("previous dreta", previous)
                if previous >= alçada:
                    gran.append("petit")
                    break
                else:
                    gran.append("gran")
                index_provisional += 1
            if gran.count("gran") == len(gran):
                visible = True
                """ print(list[index])
                print(list[index][index2])
                print("visible") """

            

            #   ==  Top ==
            index_provisional = index -1 
            index_total = index
            gran = []
            while index_provisional >= 0:
                top += 1
                previous = list[index_provisional][index2]
                print("previous top", previous)
                #print(previous)
                if previous >= alçada:
                    gran.append("petit")
                    break
                else:
                    gran.append("gran")
                index_provisional -= 1
            if gran.count("gran") == len(gran):
                visible = True

            


            #   ==  Bottom  ==
            index_provisional = index +1 
            index_total = index
            gran = []
            while index_provisional < len(list):
                bottom += 1
                previous = list[index_provisional][index2]
                print("previous bottom", previous)
                #print(previous)
                if previous >= alçada:
                    gran.append("petit")
                    print("break")
                    break
                else:
                    gran.append("gran")
                index_provisional += 1
            if gran.count("gran") == len(gran):
                visible = True

            
            
            #Final
            if visible == True:
                arbres_visibles += 1
            print("---")
            print(list[index][index2])
            print("-----------------------")
            print("esquerra", esquerra)
            print("dreta", dreta)
            print("top", top)
            print("bottom", bottom)
            a = esquerra * dreta * top*bottom
            if a > perfecte:
                perfecte = a

            
        else:
            primer = False
        index2 += 1
    index += 1
print(arbres_visibles)
print(perfecte) 