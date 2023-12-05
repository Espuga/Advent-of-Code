import threading

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



def funcio(seed):
    global result
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
primer = True
for x in range(len(seeds)):
    if anterior:
        for y in range(0, int(seeds[x])):
            z = threading.Thread(target=funcio, args=(str(int(seeds[x-1])+y),))
            z.start()

        anterior = False
    else:
        anterior = True

print("Result "+ str(result))