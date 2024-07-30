import sys
m, n = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(li)

answer = 0
while start <= end:
    mid = (start+end)//2

    cnt = 0
    for x in li:
        if x < mid:
            continue
        else:
            cnt += x//mid

    if cnt >= m:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
