import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
heapq.heapify(li)
for i in range(m):
    num1 = heapq.heappop(li)
    num2 = heapq.heappop(li)
    temp = num1+num2

    heapq.heappush(li, temp)
    heapq.heappush(li, temp)

print(sum(li))
