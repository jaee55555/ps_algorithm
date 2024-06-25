import sys
n = int(input())
numMax = 0

li = [0 for i in range(10001)]
for i in range(n):
    temp = int(sys.stdin.readline())
    li[temp] += 1
    if temp >= numMax:
        numMax = temp

for i in range(1, numMax + 1):
    if li[i] > 0:
        for j in range(li[i]):
            print(i)