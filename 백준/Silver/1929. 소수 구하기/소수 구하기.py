# 1929 소수구하기 에라토스테네스의 체 사용해서 풀기 
import math

a , b = map(int , input().split(' '))
number = [True for i in range(b+1)]

double = 0

for i in range(2 , b+1):
    if number[i] :
        if i**2 > 1000001:
            break
        else:
            k = i**2
            while k < b+1:
                number[k] = False
                k += i # 배수를 다 지움 

if a == 1: a += 1

for i in range(a , b+1 , 1):
    if number[i]: # True 일때만 숫자 출력 
        print(i)


