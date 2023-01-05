# 아래문제 선행문제 ( 누적 합 문제 ) - 11659 구간 합 구하기 4
import sys

n , test_case = map(int, sys.stdin.readline().split()) # m 은 case 횟수 
numbers = list(map(int , sys.stdin.readline().split())) # 구간 합 = 시그마의 원리를 이용함 

sigma_list = [0] # 초기 한 칸을 밀어 주어야 함 case : 1 3 
sigma = 0

for i in range(n):
    sigma += numbers[i]
    sigma_list.append(sigma) # sigma(1) , sigma(2) >>>

for i in range(test_case):
    a , b = map(int , sys.stdin.readline().split())
    print(sigma_list[b] - sigma_list[a - 1])





