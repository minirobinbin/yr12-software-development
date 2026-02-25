encyclopedia = []
pages = []

n,q = [int(x) for x in input().split(" ")]

for i in range(n):
    encyclopedia.append(int(input()))

for i in range(q):
    pages.append(int(input()))

for page in pages:
    print(encyclopedia[page-1])