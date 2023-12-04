f = open('entrades/day5_entrades.txt', 'r')
linies = f.readlines()

llista = [
    ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    ['T', 'B', 'M', 'Z', 'R'],
    ['Z', 'L', 'C', 'H', 'N', 'S'],
    ['S', 'C', 'F', 'J'],
    ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    ['M', 'Z', 'R'],
    ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
]
"""
llista = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]
"""
for linia in linies:
    x, a, y, b, z, c= linia.split()
    #   a = numero de caixes
    #   b = pila a treure
    #   c = pila a posar
    """ for i in range(0, int(a)):
        aa = llista[int(b)-1].pop()
        llista[int(c)-1].append(aa) """
    current = []
    for i in range(0, int(a)):
        aa = llista[int(b)-1].pop()
        current.insert(0, aa)
    
    for c1 in current:
        llista[int(c)-1].append(c1)
    

    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """ for i in range(0, int(a)):
        aa = llista[int(b)-1].pop()
        print(aa)
        current.insert(0, aa)
        
    llista[int(b)-1] = llista[int(b)-1] + current
    current = []
    print(llista[0])
    print(llista[1])
    print(llista[2]) """
    

for i in range(0,9):
    print(llista[i].pop() , end='')