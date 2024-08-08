import sys
from collections import deque

T = int(sys.stdin.readline())

def get_cnt(cnt, country, visited):
    deq = deque()
    start = 1
    visited[start] = True
    deq.append(start)
    # temp = country[start]
    # for t in temp:
    #     deq.append(t)
    #     visited[t] = True
    #     cnt += 1
    while deq:
        left = deq.popleft()
        temp = country[left]
        for t in temp:
            if not visited[t]:
                deq.append(t)
                visited[t] = True
                cnt += 1

    return cnt


for i in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(N+1)]
    country = [[] for _ in range(N+1)]
    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
        country[a].append(b)
        country[b].append(a)

    print(get_cnt(cnt, country, visited))
