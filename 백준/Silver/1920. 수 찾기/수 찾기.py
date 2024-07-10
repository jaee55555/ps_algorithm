from re import L
store_list_num = int(input())
store_list = list(map(int, input().split()))
store_list.sort()

check_list_num = int(input())
check_list = list(map(int, input().split()))

def check_target(target):
    left = 0
    right = len(store_list) - 1
    fact = False
    while(left <= right):
        mid = (left + right) // 2
        if store_list[mid] == target:
            fact = True
            return fact
        
        if target < store_list[mid]:
            right = mid - 1
        elif target > store_list[mid]:
            left = mid + 1
    return fact

for i in check_list:
    if check_target(i):
        print(1)
    else:
        print(0)