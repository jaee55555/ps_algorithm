from collections import deque

def solution(progresses, speeds):
    
    pg = deque(progresses)
    sp = deque(speeds)
    answer = []
    while pg:
        cnt = 0
        while pg[0] < 100:
            for i in range(len(pg)):
                pg[i] += sp[i]
        #     print(pg)
        # print("fin plus")
        left = pg[0]
        while left >= 100 and pg:
            pg.popleft()
            sp.popleft()
            cnt += 1
            if pg:
                left = pg[0]
        # print("fin popleft")
        # print(pg)
        answer.append(cnt)
    return answer