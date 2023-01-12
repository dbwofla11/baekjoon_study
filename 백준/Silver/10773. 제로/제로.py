# 10773 제로
import sys

num = int(input()) 
stack = []

for i in range(num):
    stack_num = int(input())
    if stack_num == 0:
        stack.pop() 
    else:
        stack.append(stack_num)

print(sum(stack))   