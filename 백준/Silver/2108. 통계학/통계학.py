# 2108 통계학 
import sys
from collections import Counter

num = int(input())

numbers = []

for i in range(num):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

# 최빈값 
cnt = Counter(numbers)
basic = cnt.most_common()
basic = [i for i in basic if i[1] == basic[0][1]]
most_basic = []

for i in basic:
    most_basic.append(i[0]) # 숫자만 입력

most_basic.sort()

if len(most_basic) >= 2:
    number_most_cnt = most_basic[1]
else:
    number_most_cnt = most_basic[0]

# 산술평균 
print(round(sum(numbers) / num)) # 
# 중앙값
print(numbers[len(numbers) // 2]) # 
# 최빈값
print(number_most_cnt)
# 범위
print( max(numbers) - min(numbers) ) 
