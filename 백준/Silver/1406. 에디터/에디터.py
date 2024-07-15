import sys

sen = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
left_stack = sen
right_stack = []

for _ in range(N):
    inp = sys.stdin.readline().split()
    command = inp[0]

    if command == "P":
        left_stack.append(inp[1])
    elif command == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == "B":
        if left_stack:
            left_stack.pop()

print(''.join(left_stack + right_stack[::-1]))
