import sys
n = int(input())
li = list()
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)