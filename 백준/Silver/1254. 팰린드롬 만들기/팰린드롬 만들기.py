import sys

#문자열은 한줄로 입력받을때 무조건 \n을 없애줘야한다.
S = sys.stdin.readline().rstrip()
for i in range(len(S)):
    if S[i:] == S[i:][::-1]:
        print(len(S)+i)
        break
