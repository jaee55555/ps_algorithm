import sys
from collections import deque
sys.setrecursionlimit(5000)
N, M = map(int, sys.stdin.readline().split())
li = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
cnt = 0

def dfs(start, li, visited):
    visited[start] = True
    for t in li[start]:
        if not visited[t]:
            dfs(t, li, visited)



for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

for i in range(1, len(visited)):
    if not visited[i]:
        dfs(i, li, visited)
        cnt += 1

print(cnt)
