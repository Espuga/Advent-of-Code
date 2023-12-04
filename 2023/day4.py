f = open("./inputs/input4.txt", "r")
linies = f.readlines()

result = 0

for linia in linies:
    linia = linia.strip()

    a, b = linia.split("|")
    win = a.split(":")[1].strip().split(" ")
    numbers = b.strip().split(" ")
    
    primer = True
    p = 1

    for n in numbers:
        if n in win:
            if primer:
                primer = False
                result += p
                # print(result)
            else:
                result += p
                # print(result)
                p *= 2
print(result)