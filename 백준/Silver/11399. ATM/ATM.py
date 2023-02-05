# 11399 ATM
# P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2
# [3,1,4,3,2]

# [1,2,3,4,5]

N = int(input())
time = list(map(int , input().split()))

time.sort()

sum_time = 0

for i in range(N):
    for k in range(i + 1):
        # print(sum_time)
        sum_time += time[k]

print(sum_time)
    

