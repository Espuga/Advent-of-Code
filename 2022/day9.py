#f = open('entrades/day9_entrades.txt', 'r')
f = open('entrades/day9_.txt', 'r')
linies = f.readlines()

def printar():
    print("=== Head ===")
    print("x =",position_h[0])
    print("y= ",position_h[1])
    print("== Tail ==")
    print("x =",position_t[0])
    print("y= ",position_t[1])
    print("")
    print("")

#             x  y
position_h = [0, 0]
position_t = [0, 0]
passat = []
contador = 0
cua = False
for linia in linies:
    print(linia)
    cua = False
    linia = linia.strip()
    direction, steps = linia.split()
    #print(direction+steps)
    if direction == 'D':    #down
        contador = position_h[1]
        passos = 0
        position_t[0] = position_t[0]-1
        while passos < int(steps):
            contador -= 1
            passos += 1
            position_h = [position_h[0], contador]
            if cua:
                position_t = [position_t[0], contador+1]
            else:
                cua = True
            printar()



    elif direction == 'U':  #up
        contador = position_h[1]
        position_t[1] = position_t[1]+1
        while contador < int(steps):
            contador += 1
            position_h = [position_h[0], contador]
            if cua:
                position_t = [position_t[0], contador-1]
            else:
                cua = True
            printar()



    elif direction == 'L':  #left
        contador = position_h[0]
        position_t[1] = position_t[1]+1
        passos = 0
        while passos < int(steps):
            contador -= 1
            passos += 1
            position_h = [contador, position_h[1]]
            if cua:
                position_t = [contador+1, position_t[1]]
            else:
                cua = True
            printar()



    elif direction == 'R':  #right
        contador = position_h[0]
        position_t[0] = position_t[0]-1
        while contador < int(steps):
            contador += 1
            position_h = [contador, position_h[1]]
            if cua:
                position_t = [contador-1, position_t[1]]
            else:
                cua = True
            printar()