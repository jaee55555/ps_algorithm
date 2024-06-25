import sys

N, M = map(int, sys.stdin.readline().split())
data = {}
for i in range(N):
    address, pw = sys.stdin.readline().split()
    data[address] = pw

for i in range(M):
    find_pw = sys.stdin.readline().strip()
    print(data[find_pw])
