import sys

x = int(input())
stack = []
for i in range(x):
    ops = list(map(str , sys.stdin.readline().split()))
    # num = int(ops[1])
    if ops[0] == "push":
        stack.append(int(ops[1]))
    if ops[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if ops[0] == "size":
        print(len(stack))
    if ops[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    if ops[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)