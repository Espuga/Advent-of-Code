f = open("./inputs/prova4.txt", "r")
linies = f.readlines()

result = 0


diccionari = {}

for linia in linies:
    #print("===")
    linia = linia.strip()

    a, b = linia.split("|")
    id = a.split(":")[0].split()[1]
    win = a.split(":")[1].strip().split()
    numbers = b.strip().split()

    aux = 0
    primer = True

    # Part 2
    nRepetits = len(set(numbers) & set(win))
    try:
        diccionari[int(id)]
    except:
        diccionari[int(id)] = 1

    for n in numbers:
        if n in win:
            if primer:
                primer = False
                aux = 1
            else:
                aux *= 2
        
    result += aux

    # Part 2
    #print(id, str(nRepetits))
    for x in range(1, nRepetits+1):
        try:
            diccionari[int(id)+x] += diccionari[int(id)]+1
        except:
            diccionari[int(id)+x] = diccionari[int(id)]
    
    print(diccionari)


print(result)