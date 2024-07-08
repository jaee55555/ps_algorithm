N = input()
nums = sorted(list(N))
nums.reverse()
total = 0
if '0' not in nums:
    print(-1)
else:
    for i in nums:
        total += int(i)
    if total % 3 == 0:
        print(''.join(nums))
    else:
        print(-1)