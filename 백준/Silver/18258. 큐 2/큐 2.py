import sys
from collections import deque

N = int(sys.stdin.readline())
li = deque()
for i in range(N):
    temp = list(sys.stdin.readline().split())
    word = temp[0]
    if word == "push":
        li.append(int(temp[1]))
    elif word == "pop":
        if len(li) == 0:
            print(-1)
        else:
            print(li.popleft())
    elif word == "size":
        print(len(li))
    elif word == "empty":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif word == "front":
        if len(li) > 0:
            print(li[0])
        else:
            print(-1)
    elif word == "back":
        if len(li) > 0:
            print(li[-1])
        else:
            print(-1)
