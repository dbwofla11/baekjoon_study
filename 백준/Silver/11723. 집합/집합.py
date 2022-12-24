#11723 집합 
import sys

m = int(input())
S = set()

for _ in range(m):
    msg = sys.stdin.readline().strip().split()
    
    if len(msg) == 1:
        if msg[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = msg[0], msg[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)