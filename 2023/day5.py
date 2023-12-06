import sys

def prova(result, seed):
    if seed < result:
        return int(seed)
    return result

# 896125601

f = open(sys.argv[1], "r")
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
        print("Range: "+seeds[x-1])
        for y in range(0, int(seeds[x])):
            seed = str(int(seeds[x-1])+y)
            # print("seed: "+seed)
            current = False
            for linia in linies:
                linia = linia.strip()
                if linia != "" and current == False:
                    a = linia.split()
                    if a[0][0].isdigit() and int(seed) in range(int(a[1]), int(a[1])+int(a[2])+1):
                        seed = int(seed)-int(a[1])+int(a[0])
                        current = True
                elif linia == "":
                    current = False
                            
            # print(seed)
            if primer:
                result = int(seed)
                print(result)
                primer = False
            else:
                a = prova(result, seed)
                if result != a:
                  result = a
                  print(result) 

        anterior = False
    else:
        anterior = True

print("Result "+ str(result))