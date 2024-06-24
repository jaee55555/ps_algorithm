total = int(input())
cnt = int(input())
temp = 0
for i in range(cnt):
    a, b = map(int, input().split())
    temp += a * b
if total == temp:
    print("Yes")
else:
    print("No")