n = int(input())
for i in range(n):
    num = int(input())
    word = ""
    while(num):
        temp = num % 2
        if temp == 0:
            word += "0"
        else:
            word += "1"
        num //= 2
    for _ in range(len(word)):
        if word[_] == "1":
            print(_, end=" ")

