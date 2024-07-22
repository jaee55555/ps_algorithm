import sys
N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
chk_num = []
cnt = 1000000
for i in range(len(nums)):
    if nums[i] == 1:
        chk_num.append(i)
# print(chk_num)
for i in range(0, len(chk_num)-K+1):
    temp = chk_num[i+K-1] - chk_num[i] + 1
    # print(temp)
    if temp < cnt:
        cnt = temp
if cnt == 1000000:
    print(-1)
else:
    print(cnt)
