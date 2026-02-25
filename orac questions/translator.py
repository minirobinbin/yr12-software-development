d,w = input("d and w:").split(" ")
dictionary1 = {}
messagetosend = []
while int(d) > 0:
    one,two = input("set:").split(" ")
    dictionary1[one] = two
    d = int(d)-1
while int(w) > 0:
    translator = input("trans:")
    try:
        messagetosend.append(dictionary1[translator])
    except:
        messagetosend.append("C?")
for word in messagetosend:
    print(word)