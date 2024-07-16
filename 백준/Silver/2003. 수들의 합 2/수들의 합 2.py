import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
cnt = 0
left, right = 0, 0
num_sum = li[left] + li[right]

while left <= len(li) - 1 and right <= len(li) - 1:
    if left == right:
        num_sum = li[left]

    if num_sum < M:
        right += 1
        if right <= len(li) - 1:
            num_sum += li[right]
    elif num_sum == M:
        cnt += 1
        # print(left, right)
        right += 1
        if right <= len(li) - 1:
            num_sum += li[right]
    elif num_sum > M:
        num_sum -= li[left]
        left += 1
print(cnt)
