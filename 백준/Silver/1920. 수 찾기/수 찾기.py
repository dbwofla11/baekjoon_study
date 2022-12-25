# 1920 - 수 찾기
import sys

N = int(input())
A = set(map(int , sys.stdin.readline().split())) # 요소니까 시간을 줄이기 위해서 set형이 되야함 

M= int(input())
B = list(map(int , sys.stdin.readline().split()))

for i in range(M):
    if B[i] in A:
        print(1)
    else:
        print(0)





