def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left+right) // 2
        chk = 0
        for t in times:
            chk += mid // t
            if chk >= n:
                break
            
        if chk >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer