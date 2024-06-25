def find(idx, sum_num):
    global cnt
    if idx == N:
        if sum_num == S:
            cnt += 1
        return
    find(idx + 1, sum_num + li[idx])
    find(idx + 1, sum_num)


N, S = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
find(0, 0)
if S == 0:
    cnt -= 1
print(cnt)
