import sys

S = sys.stdin.readline().rstrip()
max_num = len(S)
answer = ""
word = []
flag = False

for i in range(len(S)):
    if S[i] == "<":
        if len(word):
            temp = ''.join(word[::-1])
            answer += temp
        flag = True
        word = []
        word.append(S[i])
    elif S[i] == ">":
        word.append(S[i])
        temp = ''.join(word)
        answer += temp
        flag = False
        word = []
    elif S[i] == " " and flag == False:
        while word:
            temp = word.pop()
            answer += temp
        answer += " "
    else:
        word.append(S[i])
    # print(answer, word)
if len(word):
    answer += ''.join(word[::-1])
print(answer)
