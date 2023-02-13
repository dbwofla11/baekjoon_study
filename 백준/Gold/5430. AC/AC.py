# 5430 AC - 시간초과 해결하기 
# reverse 매번 사용 -> 뒤집는 횟수가 홀수 번일때만 뒤집도록하면 시간초과가 안뜬다 함 
from collections import deque

num = int(input())

for i in range(num):
    cmd = input()
    d = int(input())
    arr = input()[1:-1].split(',')

    dq = deque(arr)

    R_cnt = 0 # R이 몇번 나오나 체크 

    if d == 0:
        dq = []
    
    for c in cmd:
        if c == "R":
            R_cnt += 1
        elif c == "D":
            if len(dq) == 0:
                print("error")
                break
            else:
                if R_cnt % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    
    else:
        if R_cnt % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")

