maxNum = 0
sumNum = 0
for i in range(10):
    a, b = map(int, input().split())
    sumNum += b - a
    if sumNum >= maxNum:
        maxNum = sumNum
print(maxNum)
