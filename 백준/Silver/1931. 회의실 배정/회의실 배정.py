#wriitend by jaee55555
n = int(input())
li = []

cnt = 0
endPoint = 0

for i in range(n):
    a, b = map(int, input().split())
    temp = (a,b)
    li.append(temp)

li.sort(key=lambda x:(x[1], x[0]))
for start, end in li:
    if endPoint <= start:
        cnt += 1
        endPoint = end

print(cnt)
