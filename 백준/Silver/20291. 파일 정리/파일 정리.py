from collections import Counter
import sys

N = int(input())
files = []
for i in range(N):
    a, b = map(str, sys.stdin.readline().rstrip().split("."))
    files.append(b)
C = Counter(files)
sorted_C = sorted(C.items())
# print(sorted_C)
for i in sorted_C:
    print(i[0], i[1])