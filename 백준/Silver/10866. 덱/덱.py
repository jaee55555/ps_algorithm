import sys
from collections import deque
li = deque()

N = int(sys.stdin.readline())
for i in range(N):
    temp = list(sys.stdin.readline().split())
    w = temp[0]
    if w == "push_front":
        li.appendleft(int(temp[1]))
    elif w == "push_back":
        li.append(int(temp[1]))
    elif w == "pop_front":
        if len(li):
            print(li.popleft())
        else:
            print(-1)
    elif w == "pop_back":
        if len(li):
            print(li.pop())
        else:
            print(-1)
    elif w == "size":
        print(len(li))
    elif w == "empty":
        if len(li):
            print(0)
        else:
            print(1)
    elif w == "front":
        if len(li):
            print(li[0])
        else:
            print(-1)
    elif w == "back":
        if len(li):
            print(li[-1])
        else:
            print(-1)