import sys

N, M = map(int, sys.stdin.readline().split())
people = []
for i in range(N):
    group_name = sys.stdin.readline().rstrip()
    members = set()
    cnt = int(sys.stdin.readline())
    for j in range(cnt):
        members.add(sys.stdin.readline().rstrip())
    temp = (members, group_name)
    people.append(temp)

for i in range(M):
    name = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline())
    if q:
        for s in people:
            group = s[0]
            if name in group:
                print(s[1])
                break
    else:
        for s in people:
            groupN = s[1]
            if name == groupN:
                temp = sorted(list(s[0]))
                for p in temp:
                    print(p)
