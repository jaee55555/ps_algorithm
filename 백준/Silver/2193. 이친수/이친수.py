import sys
N = int(sys.stdin.readline())
if N == 1:
    print(1)
else:
    li = [0] * (N+1)
    li[0] = 0 #0의 자리 이친수는 숫자 생성 X
    li[1] = 1 #1의 자리 이친수는 1개
    li[2] = 1 #2의 자리 이친수는 1개
    for i in range(2, N+1):
        li[i] = li[i-1] + li[i-2]
    print(li[N])