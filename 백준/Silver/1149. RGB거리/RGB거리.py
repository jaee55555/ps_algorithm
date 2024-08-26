import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    li.append((temp))

for i in range(1, N):
    for j in range(len(li[i])):
        if j == 0:
            li[i][j] += min(li[i-1][1], li[i-1][2])
        elif j == 1:
            li[i][j] += min(li[i - 1][0], li[i - 1][2])
        elif j == 2:
            li[i][j] += min(li[i - 1][0], li[i - 1][1])
print(min(li[-1]))