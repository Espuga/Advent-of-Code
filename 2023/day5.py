def prova(result, seed):
    if seed < result:
        return int(seed)
    return result

f = open("./inputs/input5.txt", "r")
linies = f.readlines()

seeds = linies[0].split(":")[1].split()
linies.pop(0)
linies.pop(0)

result = 0


#seeds2 = []

anterior = False
primer = True
for x in range(len(seeds)):
    if anterior:
        for y in range(0, int(seeds[x])):
            seed = str(int(seeds[x-1])+y)
            original = seed
            # print("======= ", seed, " =======")
            trobat = False
            current = False
            for linia in linies:
                linia = linia.strip()
                if linia != "":
                    if current == False:
                        a = linia.split()
                        if a[0][0].isdigit():
                            for i in range(len(a)):
                                a[i] = int(a[i])
                            if int(seed) in range(a[1], a[1]+a[2]+1):
                                seed = int(seed)-a[1]+a[0]
                                current = True
                else:
                    current = False
                            
            # print(seed)
            if primer:
                result = int(seed)
                primer = False
            else:
                a = prova(result, seed)
                if a != result:
                    result = a
                    print(result)

        anterior = False
    else:
        anterior = True

print("Result "+ str(result))
"""
for seed in seeds2:
    original = seed
    # print("======= ", seed, " =======")
    trobat = False
    current = False
    for linia in linies:
        linia = linia.strip()
        if linia != "":
            if current == False:
                a = linia.split()
                if a[0][0].isdigit():
                    for i in range(len(a)):
                        a[i] = int(a[i])
                    if int(seed) in range(a[1], a[1]+a[2]+1):
                        seed = int(seed)-a[1]+a[0]
                        current = True
        else:
            current = False
                    
    # print(seed)
    result = int(seed) if original == seeds[0] else prova(result, seed)

print("===========")
print("Result "+ str(result))
print("===========")"""