while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        if (x/y) >= 0.99:
            print ("F")
            break
        elif (x/y) <= 0.01:
            print ("E")
            break
        else:
            print(round(float((x/y)*100)),"%", sep = "" )
            break
