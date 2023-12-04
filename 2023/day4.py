f = open("./inputs/input4.txt", "r")
linies = f.readlines()

result = 0

diccionari = {x: 1 for x in range(1, len(linies)+1)}


for linia in linies:
    linia = linia.strip()

    a, b = linia.split("|")
    id = a.split(":")[0].split()[1]
    win = a.split(":")[1].strip().split()
    numbers = b.strip().split()

    # Part 1
    aux = 0
    primer = True

    for n in numbers:
        if n in win:
            if primer:
                primer = False
                aux = 1
            else:
                aux *= 2
        
    result += aux

    # Part 2
    nRepetits = len(set(numbers) & set(win))
    diccionari.update({int(id) + x: diccionari[int(id)]+diccionari[int(id)+x] for x in range(1, nRepetits+1)})

result2 = sum(diccionari[key] for key in list(diccionari.keys()))


print(result)
print(result2)