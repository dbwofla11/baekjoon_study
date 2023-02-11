# 1021 회전하는 큐 
from collections import deque

N , M = map(int , input().split()) # 원소의 갯수 , 뽑아 내려고 하는 수 
index_li = list(map(int , input().split())) # 추출해야 하는 인덱스 리스트 받기 (처음 수니까 인덱스가 아니라 그냥 탐색해야 할 숫자로 취급 )

dq = deque(range(1,N+1))
cnt = 0 

for i in index_li: # 2 9 3 
    m = len(dq) // 2 # 중간 인덱스 

    if dq.index(i) <= m: 
        while i != dq[0]:
            dq.append(dq.popleft())
            cnt += 1
        dq.popleft()
    else:
        while i != dq[0]:
            dq.appendleft(dq.pop())
            cnt += 1
        dq.popleft()

print(cnt)
    
