# 3273 두 수의 합 

num = int(input())

numbers = list(map(int, input().split(' ')))
numbers.sort()

sum_num = int(input())
sum_cnt = 0

L , R = 0 , num - 1
while L != R:
    if numbers[L] + numbers[R] == sum_num:
        sum_cnt += 1
        L += 1
    elif numbers[L] + numbers[R] > sum_num:
        R -= 1
    
    else:
        L += 1
    

print(sum_cnt)
