import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

num_set = sorted(list(set(li)))
num_dict = dict()
for i in range(len(num_set)):
    num_dict[num_set[i]] = i

for i in range(len(li)):
    print(num_dict[li[i]], end=" ")
