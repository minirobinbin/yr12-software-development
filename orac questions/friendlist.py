friends = {}
bestlist = []
connections = int(input())

for connection in range(connections):
    first, second = input().split(" ")
    if first in friends:
        friends[first] += 1
    else:
        friends[first] = 1
    if second in friends:
        friends[second]+=1
    else:
        friends[second] = 1

most = max(friends.values())
for friend in friends:
    if friends[friend] == most:
        bestlist.append(friend)
bestlist.sort()
print(', '.join([str(x) for x in bestlist]))