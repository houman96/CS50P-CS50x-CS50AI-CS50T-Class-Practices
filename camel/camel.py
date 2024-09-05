beforestring = input("camelCase: ")
afterlist = []
for word in beforestring:
    if word.isupper():
        afterlist.append("_")
        afterlist.append(word.lower())
    else:
        afterlist.append(word)

afterstring = "".join(afterlist)
print ("snake_case:", afterstring)
