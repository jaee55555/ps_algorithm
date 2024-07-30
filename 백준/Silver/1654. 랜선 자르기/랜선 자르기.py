import sys

K, N = map(int, sys.stdin.readline().split())
li = list()
for i in range(K):
    li.append(int(sys.stdin.readline()))
li.sort()
min_num = 1
max_num = li[-1]

cnt = 0

while min_num <= max_num:
    cnt = 0
    mid = (min_num+max_num) // 2
    for l in li:
        cnt += l // mid
    if cnt >= N:
        min_num = mid + 1
    else:
        max_num = mid -1
print(min_num-1)