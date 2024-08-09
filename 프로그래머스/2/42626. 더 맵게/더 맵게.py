import heapq
from collections import deque
def solution(scoville, K):
    answer = 0
    # low = deque()
    sc = []
    
    for s in scoville:
        heapq.heappush(sc, s)
    first = heapq.heappop(sc)
    while first < K and len(sc) >= 1:
        second = heapq.heappop(sc)
        temp = first + second * 2
        
        heapq.heappush(sc, temp)
        
        answer += 1
        first = heapq.heappop(sc)
        
        
    
    if first < K:
        return -1
    else:
        return answer