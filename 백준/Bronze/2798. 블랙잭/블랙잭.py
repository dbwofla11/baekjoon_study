# 2798 블랙잭 - 브루트포스 ( 선형 탐색 )

nums , card_nums = map(int, input().split())
cards = list(map(int , input().split()))

point = 0

for i in range(0 , nums - 2): # 나머지 2장은 중복방지 
    for k in range(i + 1 , nums - 1):
        for m in range(k + 1 , nums):
            if cards[i] + cards[k] + cards[m] > card_nums:
                continue
            else:
                point = max(point , cards[i] + cards[k] + cards[m]) # max를 쓰면 if문 없이 편하게 갱신 가능 

print(point)
