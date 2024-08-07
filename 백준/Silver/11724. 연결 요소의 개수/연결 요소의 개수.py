import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
li = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
cnt = 0


def bfs(start, lli, is_visit):
    temp = lli[start]
    deq = deque()
    for t in temp:
        deq.append(t)
    while deq:
        left = deq.popleft()
        temp = lli[left]
        for t in temp:
            if not is_visit[t]:
                is_visit[t] = True
                deq.append(t)
    return is_visit


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)
# print(li)
# print(visited)

for i in range(1, len(visited)):
    if not visited[i]:
        visited = bfs(i, li, visited)
        cnt += 1

print(cnt)
