from collections import deque
import sys
n = int(input())

for i in range(n):
    temp_str = sys.stdin.readline().strip()
    left = 0
    right = 0
    result = ""
    li = deque()
    for s in range(len(temp_str)):
        if temp_str[s] == "(":
            li.append(temp_str[s])
            left += 1
        elif temp_str[s] == ")":
            right += 1
            if len(li):
                li.pop()
            else:
                result = "NO"
                break
    if result == "NO":
        print(result)
    elif left == right and len(li) == 0:
        print("YES")
    else:
        print("NO")
