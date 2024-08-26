import sys
N = int(sys.stdin.readline())
li = [0 for i in range(1001)]

li[1] = 1
li[2] = 2
li[3] = 1

for i in range(4, N+1):
    li[i] = min(li[i-1], li[i-3]) + 1

if li[N] % 2:
    print('SK')
else:
    print("CY")

