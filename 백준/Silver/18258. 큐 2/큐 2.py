# 10845 큐 
import sys
from collections import deque


num = int(input())
qu = deque([])

for i in range(num):
    msg = sys.stdin.readline().split()

    if msg[0] == "push":
        qu.append(msg[1])
    elif msg[0] == "pop":
        if qu: print(qu.popleft())
        else: print(-1)
    elif msg[0] == "size":
        print(len(qu))
    elif msg[0] == "empty":
        if qu: print(0)
        else: print(1)
    elif msg[0] == "front": 
        if qu: print(qu[0])
        else: print(-1)
    elif msg[0] == "back":
        if qu: print(qu[-1])
        else: print(-1)
    else:
        pass

