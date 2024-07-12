import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
answer = deque(sorted(a-b))
print(len(answer))
while answer:
    print(answer[0], end=' ')
    answer.popleft()