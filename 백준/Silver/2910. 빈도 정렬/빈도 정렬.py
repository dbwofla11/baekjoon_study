# 2910 빈도정렬 
# 정렬 순서 ( 빈도수가 많은것 1순위 , 먼저 나온거 2순위 )
import sys

n , c = map(int , input().split())
nums = list(map(int , input().split()))

cnt = dict()

idx = 0
for i in nums:
    if i in cnt:
        cnt[i][0] += 1
    else:
        cnt[i] = [1 , idx] # [cnt , idx]
        idx += 1 

sorting_nums = [ [ i , k ] for i , k in cnt.items() ]
# print(sorting_nums)
sorting_nums.sort( key = lambda x : ( -x[1][0]  , x[1][1] ))
# print(sorting_nums)

res = []
for i , k in sorting_nums: 
    res += [i]*k[0]

print(*res)