filename = input("Filename : ").lower().split(".")

if filename[-1]:
    word = filename[-1].lower().strip()
else:
    print ("application/octet-stream")

if word == "gif":
    print ("image/gif")
elif word == "jpeg" or word == "jpg":
    print ("image/jpeg")
elif word == "png":
    print ("image/png")
elif word == "pdf":
    print ("application/pdf")
elif word == "txt":
    print ("text/plain")
elif word == "zip":
    print ("application/zip")
else:
    print ("application/octet-stream")
