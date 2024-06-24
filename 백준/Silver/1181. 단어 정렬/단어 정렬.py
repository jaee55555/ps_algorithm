n = int(input())
li = set(input() for i in range(n))
li = list(li)
li.sort()
li.sort(key=lambda x: len(x))
for i in li:
    print(i)