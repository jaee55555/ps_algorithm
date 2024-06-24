hour, minute = map(int, input().split())
time = int(input())
temp = minute + time
if temp >= 60:
    while temp // 60:
        t = temp // 60
        hour += t
        temp %= 60
minute = temp
if hour >= 24:
    hour -= 24
print(hour, minute)