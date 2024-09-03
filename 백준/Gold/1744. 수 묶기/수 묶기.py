import sys

N = int(sys.stdin.readline())
positive = []
negative = []
answer = 0
for i in range(N):
    temp = int(sys.stdin.readline())
    if temp > 0:
        positive.append(temp)
    else:
        negative.append(temp)
positive.sort()
negative.sort(reverse=True)

#양수 연산
while len(positive) > 0:
    if len(positive) == 1:
        answer += positive[0]
        break
    num1 = positive.pop()
    num2 = positive.pop()
    plus = num1 + num2
    multi = num1 * num2

    if plus < multi:
        answer += multi
    else:
        answer += plus


#음수 연산
while len(negative) > 0:
    if len(negative) == 1:
        answer += negative[0]
        break
    num1 = negative.pop()
    num2 = negative.pop()
    plus = num1 + num2
    multi = num1 * num2

    if plus < multi:
        answer += multi
    else:
        answer += plus

print(answer)
