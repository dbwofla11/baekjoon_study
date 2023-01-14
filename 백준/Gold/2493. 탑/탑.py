# 2493 탑 - mv
n = int(input())
arr = list(map(int , input().split()))  # ex) 6 9 5 7 4
stack = [[ n - 1 , arr[-1] ]]
answer = [0] * n

for i in range(n - 2 , -1 , -1):

    if stack[-1][1] < arr[i]: # arr의 초기 4 와 7 
        while stack and stack[-1][1] < arr[i]:
            answer[stack.pop()[0]] = 1 + i # 쏜 타워 , 맞는 타워 인덱스 
            # print(answer , "while")
        stack.append([i , arr[i]]) # arr에서 pop한거 stack에 append
        # print("append if")
    else:
        stack.append([i , arr[i]]) # 조건 안될때는 스택을 쌓음 
        # print("else")

for i in answer:
    print(i , end = " " ) 
