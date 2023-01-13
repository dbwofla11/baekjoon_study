# 1874 스택 수열 
# 1 2 3 4 5 6 7 8 현재 수열 
# 4 3 6 8 7 5 2 1 만들고자 하는 수열 

# 스택의 조건이 오름차순 push 
# 1) 현재 수열의 원소가 더 크다 -> push
# 2) 현재 수열의 원소가 만들고자 하는 수열의 수와 같다 -> pop
# 3) 스택에 들어갈때 마지막 원소가 더 크다  1 2 5 3 4 -> 5땜에 안됨 
import sys
num = int(input())

num_list = []
for i in range(num):
    num_list.append(int(sys.stdin.readline()))
    # num_list.append(int(input()))

# + - 만들기 

op_list = [] # + - 저장할 리스트
stack = [] # 스택 

stack_cnt = 0
# index = 0
no_bool = 0

for index in range(num):
    
    while num_list[index] > stack_cnt: # 1 num의 원소가 넣고자 하는 스택 cnt보다 클때 push 
        stack_cnt += 1
        stack.append(stack_cnt)
        op_list.append("+")
    
    if stack[-1] == num_list[index]:
        op_list.append("-")
        stack.pop()
    elif stack[-1] != num_list[index] :
        print("NO")
        no_bool = 1
        break

if no_bool != 1:
    for i in op_list:
        print(i)
         
