f = open('entrades/day2_entrades.txt', 'r')
linies = f.readlines()
"""
a, x = Rock
b, y = Paper
c, z = Scissors


"""
points = 0

for linia in linies:
    a, b = linia.split()
    # Punts per tria
    if a == "A":
        points += 1
    elif a == "B":
        points += 2
    elif a == "C":
        points += 3

    # Punts per victoria
    if a == "A" and b == "Z" or a == "C" and b == "Y" or a == "B" and b == "X":
        points += 0
    elif a == "A" and b == "X" or a == "B" and b == "Y" or a == "C" and b == "Z":
        points += 3
    else:
        points += 6
print(points)