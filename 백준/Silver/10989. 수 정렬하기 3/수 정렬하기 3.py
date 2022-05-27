import sys
n = int(input()) # 맨 처음 숫자 
check_ls = [0] * 10001 # 메모리 활당 

for _ in range(n):
    num = int(sys.stdin.readline()) # 빠르게 입력받기 
    check_ls[num] = check_ls[num] + 1  # 체크를 하게되면 

for i in range(10001):
    if check_ls[i] != 0 :
        for _ in range(check_ls[i]):
            print(i)