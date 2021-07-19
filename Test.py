mylist = [(1,2,3), (4,5,6), (7,8,9)]

for i, tuple in enumerate(mylist):
    for j in range(len(tuple)):
        tuple[j] += 1

print(mylist)