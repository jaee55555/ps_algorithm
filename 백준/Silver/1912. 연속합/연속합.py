import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    if li[i - 1] > 0:
        li[i] += li[i - 1]
# print(li)
print(max(li))