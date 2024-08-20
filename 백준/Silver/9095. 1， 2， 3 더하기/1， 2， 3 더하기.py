import sys

def solve(n):
    # DP 테이블 초기화 (충분히 큰 크기로)
    dp = [0] * (n + 1)

    # 초기 조건 설정
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    if n > 2:
        dp[3] = 4

    # 점화식을 이용하여 DP 테이블 채우기
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # n을 만들 수 있는 경우의 수 반환
    return dp[n]


T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    print(solve(n))
