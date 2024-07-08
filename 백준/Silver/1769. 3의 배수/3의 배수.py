string = input()
cnt = 0
while len(string) > 1:
    temp = 0
    for i in range(len(string)):
        temp += int(string[i])
    string = str(temp)
    cnt += 1
print(cnt)

if int(string) % 3 == 0:
    print("YES")
else:
    print("NO")


