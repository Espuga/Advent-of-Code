#f = open('entrades/day10_entrades.txt', 'r')
f = open('entrades/day10_.txt', 'r')
linies = f.readlines()
cycles = 0
x = 1
total = 0

def comprobar():
    global total
    if cycles == 20:
        print(cycles, x)
        total += (cycles*x)
    elif cycles == 60:
        print(cycles, x)
        total += (cycles*x)
    elif cycles == 100:
        print(cycles, x)
        total += (cycles*x)
    elif cycles == 140:
        print(cycles, x)
        total += (cycles*x)
    elif cycles == 180:
        print(cycles, x)
        total += (cycles*x)
    elif cycles == 200:
        print(cycles, x)
    elif cycles == 220:
        print(cycles, x)
        total += (cycles*x)

for linia in linies:
    linia = linia.strip()
    current = linia.split()
    if current[0] == 'addx':
        cycles += 1
        comprobar()
        x += int(current[1])
        cycles += 1
        comprobar()
    else:
        cycles += 1
        comprobar()
    
    
print(total)