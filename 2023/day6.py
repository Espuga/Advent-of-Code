f = open("./inputs/input6.txt", "r")
linies = f.readlines()

# Part 1
result = 1

segons = linies[0].split(":")[1].split()
metres = linies[1].split(":")[1].split()

for i in range(len(segons)):
  segon = segons[i]
  metre = metres[i]

  # Versió 1
  """intents = 0
  for x in range(0, int(segon)+1):
    aux = (int(segon)-x)*x
    if aux > int(metre):
      intents += 1"""
  intents = sum(1 for x in range(0, int(segon)+1) if(int(segon)-x)*x > int(metre))

  result *= intents

#print(result)

# Part 2
segon = linies[0].strip().split(":")[1].replace(" ", "")
metre = linies[1].strip().split(":")[1].replace(" ", "")

# Versió 1
"""intents = 0
for x in range(0, int(segon)+1):
  aux = (int(segon)-x)*x
  if aux > int(metre):
    intents += 1"""
# Versió 2
intents = sum(1 for x in range(0, int(segon)+1) if(int(segon)-x)*x > int(metre))

print(intents)
