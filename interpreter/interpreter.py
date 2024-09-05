expression = input("Expression: ")
x, y, z = expression.split()
x = float(x)
z= float(z)

if y =="+":
    r = x + z
    print("{:.1f}".format(r))
elif y =="-":
    r = x - z
    print("{:.1f}".format(r))
elif y =="/":
    r = x / z
    print("{:.1f}".format(r))
elif y =="*":
    r = x * z
    print("{:.1f}".format(r))
