N, M = map(int, input().split())
set_a = set()
answer = []
for i in range(N):
    set_a.add(input())
for j in range(M):
    temp = input()
    if temp in set_a:
        answer.append(temp)
print(len(answer))
answer.sort()
for x in answer:
    print(x)