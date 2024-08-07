import sys
from collections import deque
sys.setrecursionlimit(5000) #재귀호출 한계 늘려주기

N, M = map(int, sys.stdin.readline().split())
li = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
cnt = 0


def bfs(start, lli, is_visit):
    #출발하는 노드에 연결된 노드들을 deq 에추가
    is_visit[start] = True

    temp = lli[start]
    deq = deque()
    for t in temp:
        deq.append(t)

    #그래프 순회 시작
    while deq:
        left = deq.popleft()
        temp = lli[left]
        for t in temp:
            if not is_visit[t]:
                is_visit[t] = True # 방문 체크
                deq.append(t) # 방문하지 않은 노드만 deq에 추가
    return is_visit

def dfs(start, li, visited):
    visited[start] = True
    for t in li[start]:
        #방문하지 않은 노드일 경우, 재귀적으로 방문처리해주기
        if not visited[t]:
            dfs(t, li, visited)



for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향 그래프이기때문에 양쪽에 노드 기록 남기기
    li[a].append(b)
    li[b].append(a)

#0번 노드는 없기때문에 1번부터 순회
for i in range(1, len(visited)):
    #방문하지 않은 노드일 경우, bfs나 dfs해주기
    #bfs나 dfs할때마다 cnt 증가
    if not visited[i]:
        #visited = bfs(i, li, visited)
        dfs(i, li, visited)

        cnt += 1

print(cnt)
