# written by jaee55555
n, m = map(int, input().split())
answer = 1
temp = 1
m1 = m2 = 0
if m <= n-m:
    m1 = m
    m2 = n-m
else:
    m1 = n-m
    m2 = m

for i in range(n, m2, -1):
    answer *= i
for i in range(2, m1+1):
    temp *= i
print(answer // temp)
