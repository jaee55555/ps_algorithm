n1 = int(input())
n2 = int(input())
temp = n2
for i in range(3):
    print(n1 * (temp%10))
    temp //= 10
print(n1*n2)