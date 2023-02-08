# 이것이 코딩테스트다 내용 정리 
# 예제 1) 거스름 돈 

# 5585 거스름돈 

s = int(input())

money = 1000 - s 
num = 0
coin = [500 , 100 , 50 , 10 , 5 , 1]

for i in coin:
    num += money // i
    money = money % i

print(num)
