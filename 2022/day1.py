
#   Part 1
""" 
f = open('day1_entrades.txt', 'r')
linies = f.readlines()
previous = 0
suma = 0
for linia in linies:
    linia = linia.strip()
    if linia != "":
        suma += int(linia)
    else:
        if suma > previous: 
            previous = suma
        suma = 0
print(previous)
"""
#   Part 2

f = open('entrades/day1_entrades.txt', 'r')
linies = f.readlines()
primer = 0
segon = 0 
tercer = 0
suma = 0
for linia in linies:
    linia = linia.strip()
    if linia != "":
        suma += int(linia)
    else:
        if suma > primer:
            tercer = segon
            segon = primer
            primer = suma
        elif suma > segon:
            tercer = segon
            segon = suma
        elif suma > tercer: 
            tercer = suma
        suma = 0
resultat = primer + segon + tercer
print(resultat)
