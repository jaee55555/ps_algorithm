from itertools import combinations

li = input().split()
while len(li) > 1:
    lii = li[1:]
    for i in combinations(lii, 6):
        for j in range(len(i)):
            print(i[j], end=" ")
        print()
    li = input().split()
    print()

