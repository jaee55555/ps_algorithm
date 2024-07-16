import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
left = 0
right = N - 1
min_num = li[left] + li[right]

while left < right:
    temp = li[left] + li[right]
    if abs(temp) < abs(min_num):
        min_num = temp
    else:
        if abs(li[left]) > abs(li[right]):
            left += 1
        else:
            right -= 1
print(min_num)