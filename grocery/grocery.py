grocery = []
while True:
    try:
        item = input()
    except EOFError:
        print (" ")
        break
    else:
        grocery.append(item)

groceryset = set(grocery)
grocerydict = dict()
for fruit in grocery:
    if fruit not in grocerydict:
        grocerydict[fruit] = 1
    else:
        grocerydict[fruit] += 1

for f in grocerydict:
    print (grocerydict[f], f.upper())
