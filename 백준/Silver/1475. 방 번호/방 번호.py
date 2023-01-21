import math as m
n = input()
n_cnt = [0,0,0,0,0,0,0,0,0,0]
for i in n:
    n_cnt[int(i)] += 1

n_cnt[6] , n_cnt[9] = m.ceil((n_cnt[6] + n_cnt[9]) / 2) , m.ceil((n_cnt[6] + n_cnt[9]) / 2)

print(max(n_cnt))