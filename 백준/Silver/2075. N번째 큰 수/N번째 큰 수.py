import sys
import heapq

N = int(sys.stdin.readline())
nums = []


for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for t in temp:
        if len(nums) < len(temp):
            heapq.heappush(nums, t)
        else:
            if nums[0] < t:
                heapq.heappop(nums)
                heapq.heappush(nums, t)
print(nums[0])