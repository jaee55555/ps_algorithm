import math
from collections import deque

N, S = map(int, input().split())
li = list(map(int, input().split()))

dis = deque([abs(S-i) for i in li])

while len(dis) > 1:
    a = dis.popleft()
    b = dis.popleft()
    dis.append(math.gcd(a,b))

print(dis.popleft())