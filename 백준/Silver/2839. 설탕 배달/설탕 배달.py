# 2839 설탕 배달 

num = int(input())
bag = 0

while num >= 0:
    if num % 5 == 0:
       bag += num // 5
       print(bag)
       break
    num -= 3
    bag += 1
else:
    print(-1) # 설탕이 마이너스가 되면 -1 출력 예) 4 
    



    
