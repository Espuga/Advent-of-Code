with open("./inputs/input2.txt", "r") as f:
    linies = f.readlines()

    result = 0

    for linia in linies:
        part1, part2 = linia.split(": ")
        id = part1.split(" ")[1]
        sets = part2.split("; ")
        # posar = True
        red = 1
        green = 1
        blue = 1
        for set in sets:
            set = set.strip()
            for opcio in set.split(", "):
                sOpcio = opcio.split(" ")
                if sOpcio[1] == "red" and red < int(sOpcio[0]):
                    red = int(sOpcio[0])
                elif sOpcio[1] == "green" and green < int(sOpcio[0]):
                    green = int(sOpcio[0])
                elif sOpcio[1] == "blue" and blue < int(sOpcio[0]):
                    blue = int(sOpcio[0])
        result += red*green*blue 
                
        """     if sOpcio[1] == "red" and int(sOpcio[0]) > 12:
                    posar = False
                    break
                elif sOpcio[1] == "green" and int(sOpcio[0]) > 13:
                    posar = False
                    break
                elif sOpcio[1] == "blue" and int(sOpcio[0]) > 14:
                    posar = False
                    break """
        """ if posar:
            result += int(id) """

    print(result)