N, M = map(int, input().split())
li = [0 for i in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    for j in range(a, b+1):
        li[j] = c

for _ in range(1, N+1):
    print(li[_], end=" ")