# 2164 카드 2 
from collections import deque

num = int(input())
qu = deque(x for x in range(1,num+1))

while True:
    tmp = qu.popleft()
    if qu:
        a = qu.popleft()
        qu.append(a)
    else:
        print(tmp)
        break
