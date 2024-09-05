nameslist = []

while True:
    try:
        name = input("Name: ")
        nameslist.append(name)
        nameslist.append(", ")

    except EOFError:
        nameslist.pop(len(nameslist) - 1)
        print()

        if len(nameslist) == 3:
            nameslist[(len(name_list) - 2)] = ' and '

        elif len(nameslist) > 3:
            nameslist[(len(nameslist) - 2)] = ', and '

        print("Adieu, adieu, to", end=' ')

        for i in range(len(nameslist)):
            print(f"{nameslist[i]}", end='')

        print()

        exit()
