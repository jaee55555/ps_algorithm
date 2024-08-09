from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    nums = deque([i for i in range(len(priorities))])
    total = []

    while priorities:
        max_num = max(priorities)
        left = priorities.popleft()
        while left != max_num:
            priorities.append(left)
            nums.append(nums.popleft())
            left = priorities.popleft()
        total.append(nums.popleft())

    for i in range(len(total)):
        if total[i] == location:
            return (i+1)