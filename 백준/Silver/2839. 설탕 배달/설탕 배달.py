import sys

N = int(sys.stdin.readline())


if N % 5 == 0:
    print(N//5)
else:
    answer = 0
    while N:
        N -= 3
        answer += 1

        if N % 5 == 0:
            answer += N // 5
            print(answer)
            break
        elif N == 1 or N ==2:
            print(-1)
            break
        elif N == 0:
            print(answer)
            break
