amountdue = 50
while amountdue > 0:
    print ("Amount Due:", amountdue)
    insertcoin = int(input("Insert Coin: "))
    amountdue -= insertcoin
else:
    print ("Change Owed:", -(amountdue))
