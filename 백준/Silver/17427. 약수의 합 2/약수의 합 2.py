# 17427 약수의 합 

num = int(input())

sum = 0 
for i in range(1,num+1):
    sum += ( num // i ) * i

print(sum)