import heapq
import sys

N = int(input())

li = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(li):
            print(heapq.heappop(li))
        else:
            print(0)
    else:
        heapq.heappush(li, num)
