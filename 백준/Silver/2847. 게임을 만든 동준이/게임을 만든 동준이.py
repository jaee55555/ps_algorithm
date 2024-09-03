import sys
from collections import deque

N = int(sys.stdin.readline())
li = deque()
cnt = 0
for i in range(N):
    temp = int(sys.stdin.readline())
    li.appendleft(temp)

for i in range(1, N):
    if li[i] >= li[i-1]:
        while li[i] >= li[i-1]:
            li[i] -= 1
            cnt += 1
# print(li)
print(cnt)

