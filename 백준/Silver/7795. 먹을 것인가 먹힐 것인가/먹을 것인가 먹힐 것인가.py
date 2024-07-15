import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    A, B = map(int, sys.stdin.readline().split())
    list_a = sorted(list(map(int, sys.stdin.readline().split())))
    list_b = sorted(list(map(int, sys.stdin.readline().split())))

    j = 0
    for i in range(A):
        while j < B and list_b[j] < list_a[i]:
            j += 1
        cnt += j

    print(cnt)
