import sys
n = int(sys.stdin.readline())
li = [0,1]
for i in range(2,n+1):
    temp = li[i-2] + li[i-1]
    li.append(temp)
print(li[n])