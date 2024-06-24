li = list(map(int, input().split()))
li.sort()
if li[0] == li[1] == li[2]:
    print(10000 + li[0]*1000)
elif li[0] == li[1]:
    print(1000 + li[0]*100)
elif li[1] == li[2]:
    print(1000 + li[1]*100)
elif li[0] == li[2]:
    print(1000 + li[0] * 100)
else:
    print(max(li) * 100)