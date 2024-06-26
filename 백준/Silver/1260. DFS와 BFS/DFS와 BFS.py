from collections import deque

# 0626
# written by jaee55555
def dfs(start):
    visit_dfs[start] = True
    for i in range(len(graph[start])):
        node = graph[start][i]
        if not visit_dfs[node]:
            visit_dfs[node] = True
            total_dfs.append(node)
            dfs(node)
    return

def bfs():
    while len(total_bfs):
        temp = total_bfs.popleft()
        print(temp, end=" ")
        for x in range(len(graph[temp])):
            idx = graph[temp][x]
            if not visit_bfs[idx]:
                visit_bfs[idx] = True
                total_bfs.append(graph[temp][x])
    print()
    return



N, M, V = map(int, input().split())
visit_dfs = [False] * (N + 1)
total_dfs = deque([V])
# visit_dfs[V] = True

visit_bfs = [False] * (N + 1)
total_bfs = deque([V])
visit_bfs[V] = True

graph = [[] for _ in range(N + 1)]

for i in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node1].sort()

    graph[node2].append(node1)
    graph[node2].sort()

dfs(V)

for _ in range(len(total_dfs)):
    if _ < (len(total_dfs) - 1):
        print(total_dfs[_], end=" ")
    else:
        print(total_dfs[_])
# print(visit_dfs)
bfs()
# print(visit_bfs)

