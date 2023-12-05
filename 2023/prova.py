def prova(result, seed):
    if seed < result:
        return int(seed)
    return result

f = open("./inputs/prova5.txt", "r")
linies = f.readlines()

seeds = linies[0].split(":")[1].split()
linies.pop(0)
linies.pop(0)

result = 0

def comprovar():
    pass

for seed in seeds:
    original = seed
    print("======= ", seed, " =======")
    trobat = False
    for linia in linies:
        linia = linia.strip()
        if linia != "":
            a = linia.split()
            if a[0][0].isdigit():
                for i in range(len(a)):
                    a[i] = int(a[i])
                if int(seed) in range(a[1], a[1]+a[2]+1):
                    seed = int(seed)-a[1]+a[0]
    print(seed)
    result = int(seed) if original == seeds[0] else prova(result, seed)

print("===========")
print("Result "+ str(result))
print("===========")