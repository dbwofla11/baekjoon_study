# 24416 알고리즘 수업 - 피보나치 수 1
import sys

num = int(input())

def fibo_recur(num):
    global cnt_recur 
    if num == 1 or num == 2:
        cnt_recur += 1
        return 1
    else:
        return fibo_recur(num -1) + fibo_recur(num - 2)

dp = [0 for i in range(num+1)]
def fibo_dp(num):
    global cnt_dp
    if num == 1 or num == 2:
        return 1
    if dp[num] != 0:
        return dp[num]
    
    cnt_dp += 1
    dp[num] = fibo_dp(num - 1) + fibo_dp(num - 2)
    return dp[num]


cnt_recur = 0
cnt_dp = 0

fibo_recur(num)
fibo_dp(num)

print(cnt_recur , cnt_dp)