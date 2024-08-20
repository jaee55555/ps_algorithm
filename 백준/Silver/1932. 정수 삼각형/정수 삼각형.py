import sys

N = int(sys.stdin.readline())
li = []
for n in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(N-len(temp)):
        temp.append(0)
    li.append(temp)

for i in range(1, len(li)):
    for j in range(len(li)):
        if j == len(li) - 1:
            li[i][j] += li[i-1][j-1]
        else:
            num1 = li[i][j] + li[i-1][j]
            num2 = li[i][j] + li[i-1][j-1]
            li[i][j] = max(num1, num2)

if N == 1:
    print(li[0][0])
else:
    print(max(li[-1]))
