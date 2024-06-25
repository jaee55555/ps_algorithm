def print_nums(idx):
    global string
    if idx == M:
        for x in range(len(arr)):
            string += str(arr[x]) + " "
        print(string)
        string = ""
        return

    for i in range(N):
        arr[idx] = i+1
        print_nums(idx+1)


N, M = map(int, input().split())
arr = [0] * M
string = ""

print_nums(0)
