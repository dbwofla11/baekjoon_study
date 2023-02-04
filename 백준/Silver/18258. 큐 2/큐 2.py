# 18258 큐 2
import sys
from collections import deque

n = int(input())
q = deque([])

for i in range(n):
    ops = list(map(str , sys.stdin.readline().split()))
    if ops[0] == "push":
        q.append(ops[1])
    if ops[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    if ops[0] == "size":
        print(len(q))
    if ops[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    if ops[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    if ops[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)