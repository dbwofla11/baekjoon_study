n = int(input()) # 216 , 0 ~ 216 

for i in range(n): # 1 , 10 , 100 EX) 123 => 1 + 2 + 3 + (123 = i) 
    temp = sum(map(int , str(i))) # 각 자리수 다 더하기 
    sum_su = temp + i
    if sum_su == n:
        print(i)
        break
else:
    print(0)


# n = 300 / 0 ~ 300 다 탐색  




