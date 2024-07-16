import sys
from collections import Counter
from collections import deque

N, C = map(int, sys.stdin.readline().split())
nums = Counter(list(map(int, sys.stdin.readline().split())))
numbers = list(nums.items())
numbers.sort(key=lambda x:x[1], reverse=True)
for box in numbers:
    cnt = box[1]
    num = box[0]
    for i in range(cnt):
        print(num, end=' ')