# 11652 카드 
# 딕셔너리 정렬 연습 ( 활용 )
import sys
num = int(input())
cards = dict()

for i in range(num):
    n = int(sys.stdin.readline())
    if cards.get(n): # 딕셔너리의 n의 value나 key가 존재하는 가 여부 .get()이 다 키와 벨류 둘다 가져오는 거임 
        cards[n] += 1
    else:
        cards[n] = 1

sorted_card = sorted(cards.items())
# print(list(sorted_card)[0])
max_num , max_cnt = 0 , 0 
for num , cnt in sorted_card:
    if max_cnt < cnt:
        max_cnt = cnt
        max_num = num

print(max_num)
