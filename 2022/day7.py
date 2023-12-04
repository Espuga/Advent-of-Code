#f = open('entrades/day7_entrades.txt', 'r')
f = open('entrades/day7_.txt', 'r')
linies = f.readlines()

#   part 1
contador = 0
current = 0
for linia in linies:
    linia = linia.strip()
    if linia == "$ cd /":
        pass
    else:
        list = linia.split()
        if list[1] == "cd":
            if current <= 100000:
                print(contador, "+", current)
                contador += current
                
            current = 0
        elif list[0].isdigit() == True:
            current += int(list[0])

print(contador)




















""" contador = 0
list = []
pr = 0 
provisional = []
for linia in linies:
    current = linia.strip().split()
    if current[1] == "cd":
        if pr <= 100000:
            contador += pr
        provisional.append(pr)
        pr = 0
    if current[0].isdigit() == True:
        pr += int(current[0])
    current = []


for c1 in provisional:
    if c1 <= 100000:
        print(contador, " + ", c1)
        contador += c1  """
#print(contador)