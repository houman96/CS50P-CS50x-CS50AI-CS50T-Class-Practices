number = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if number == "42":
    print ("Yes")
elif number == "Forty Two" or number =="forty-two" or number == "forty two" or number =="Forty-Two":
    print ("Yes")
else:
    print ("No")
