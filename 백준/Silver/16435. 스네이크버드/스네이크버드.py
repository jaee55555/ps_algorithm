import sys

N, L = map(int, sys.stdin.readline().split())
li = sorted(list(map(int, sys.stdin.readline().split())))

for i in li:
    if i <= L:
        L += 1
    else:
        break

print(L)