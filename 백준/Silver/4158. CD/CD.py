import sys
N, M = map(int, sys.stdin.readline().split())
while N != 0 and M != 0:
    cnt = 0
    n_set = set()
    for i in range(N):
        n_set.add(int(sys.stdin.readline()))
    for i in range(M):
        temp = int(sys.stdin.readline())
        if temp in n_set:
            cnt += 1
    print(cnt)
    N, M = map(int, sys.stdin.readline().split())