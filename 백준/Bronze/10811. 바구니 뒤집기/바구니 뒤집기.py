N, M = map(int, input().split())
li = [i for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    temp = li[a:b+1]
    temp = temp[::-1]
    for j in range(a, b+1):
        li[j] = temp[j-a]

for _ in range(1, N+1):
    print(li[_], end=" ")