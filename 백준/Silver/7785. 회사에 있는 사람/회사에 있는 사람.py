N = int(input())
people = set()
while(N):
    name, behavior = input().split()
    if behavior == "enter":
        people.add(name)
    else:
        people.remove(name)

    N -= 1

pp = sorted(list(people), reverse=True)
for p in pp:
    print(p)

