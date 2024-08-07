import sys
from collections import deque

sys.setrecursionlimit(10**7)  # 재귀호출 한계 늘려주기

answer = 0
n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
lines = int(sys.stdin.readline())
li = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

def dfs(start, end, li, visited, depth):
    temp = li[start]
    visited[start] = True
    for t in temp:
        if t == end:
            return depth
        elif not visited[t]:
            result = dfs(t, end, li, visited, depth+1)
            if result != -1:
                return result
    return -1


for i in range(lines):
    a, b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)
# print(li)

print(dfs(start, end, li, visited, 1))
