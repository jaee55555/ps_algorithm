import sys
S = sys.stdin.readline()

pre = S[0]
zero = 0
one = 0

for i in range(1, len(S)):
    if pre != S[i]:
        if pre == "0":
            zero += 1
        else:
            one += 1
        pre = S[i] #이전숫자 갱신
print(min(zero, one))