# 10866 덱 구현 
import sys
from collections import deque

num = int(input())

dq = deque()

for i in range(num):
    msg = sys.stdin.readline().split()

    if msg[0] == "push_front":
        dq.appendleft(msg[1])

    elif msg[0] == "push_back":
        dq.append(msg[1])
    
    elif msg[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
        
    elif msg[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    
    elif msg[0] == "size":
        print(len(dq))
    
    elif msg[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    
    elif msg[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    
    elif msg[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    
    else:
        pass