string = input()
cnt = len(string)
alpha = ["", "", ["A", "B", "C"], ["D", "E", "F"],
         ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"],
         ["P", "Q", "R","S"], ["T", "U", "V"], ["W","X","Y","Z"]]
for i in range(len(string)):
    charAlpha = string[i]
    for j in range(1, 10):
        if charAlpha in alpha[j]:
            cnt += j
print(cnt)