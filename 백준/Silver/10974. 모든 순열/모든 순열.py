from itertools import permutations

n = int(input())
li = [i for i in range(1,n+1)]
for i in permutations(li, n):
    for j in range(len(i)):
        print(i[j], end=' ')
    print()
    