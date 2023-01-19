# 4949 균형잡힌 세상 

import sys
lines = sys.stdin.readlines()
for line in lines[:-1]:
    stack = []
    for text in line:
        if text in '([':
            stack.append(text)
        elif text == ']':
            if not stack or stack.pop() != '[':
                print("no")
                break
        elif text == ')':
            if not stack or stack.pop() != '(':
                print("no")
                break
        elif text == '.':
            if stack:
                print("no")
            else:
                print("yes")
