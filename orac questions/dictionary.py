dictionary = {}
messagetosend = []
def running(inpit):
    if " " in inpit:
        one,two = inpit.split(" ")
        dictionary[int(one)] = two
    else:
        print(dictionary[int(inpit)])
setup = input("d and w:")
d,w = setup.split(" ")
trackd = 0
trackw = False
while True:
    if int(trackd) == int(d):
        trackw = True
    else:
        if trackw != True:
            trackd = trackd + 1
            print(trackd,d)
            inpit = input("set:")
        else:
            inpit = input("w:")