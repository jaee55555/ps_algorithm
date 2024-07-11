from collections import deque

N = int(input())
li = list(map(int, input().split()))
M = int(input())
m = M
cnt = 0
sum_num = sum(li)
max_num = 0

if sum_num <= M:  # 예산 이내일때 최댓값 바로 출력
    print(max(li))
else:
    li.sort()

    li = deque(li)
    pop_num = li.popleft()
    while len(li):
        m -= pop_num
        # print(li)
        if len(li):
            mid_num = m // len(li)
            # print(pop_num, mid_num, li)
            if mid_num >= pop_num and mid_num >= max_num:
                max_num = mid_num
        pop_num = li.popleft()

    if max_num == 0:
        max_num = M // N
        print(max_num)
    else:
        print(max_num)
