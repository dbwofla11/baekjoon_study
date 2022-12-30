# 1475 방 번호 
import math as m
num_cnt = [0 for i in range(10)]

a = list(map(int, input()))

for i in a:
    num_cnt[i] += 1

num_cnt[6] , num_cnt[9] = m.ceil((num_cnt[6] + num_cnt[9]) / 2) , m.ceil((num_cnt[6] + num_cnt[9]) / 2)



print(max(num_cnt))
