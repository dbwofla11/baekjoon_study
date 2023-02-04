# 재귀 연습 - 피보나치 수열 
n = int(input())

def fibo(n):
    if n <= 1: # 재귀 필수 조건 ( 종료 조건 )
        return n # 리턴이 끝내는거 
    else:
        return fibo(n-1) + fibo(n-2) # 계속 함수 불러오기 


print(fibo(n))