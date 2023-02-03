# 11047 동전 0

N , K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

cnt = 0
for i in reversed(coin):
    cnt += K//i # 제일 큰 거 부터 나누기 
    K = K%i # 거스름돈 

print(cnt)