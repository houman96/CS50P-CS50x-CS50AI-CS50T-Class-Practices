greet = input("Greeting: ").lower().split()

if greet[0]:
    word = greet[0].strip()

if word == "hello":
    print ("$0")
elif word.startswith("h") and word != "hello":
    print ("$20")
else:
    print ("$100")
