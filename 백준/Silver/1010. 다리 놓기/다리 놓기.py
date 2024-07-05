T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    answer = 1
    for j in range(M, M-N, -1):
        answer *= j
    for m in range(2, N+1):
        answer //= m

    print(answer)