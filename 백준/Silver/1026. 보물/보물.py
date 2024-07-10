N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
# B.sort(reverse=True)
total = 0
for i in range(N):
    max_b = max(B)
    total += A[i] * max_b
    B.pop(B.index(max_b))
print(total)
