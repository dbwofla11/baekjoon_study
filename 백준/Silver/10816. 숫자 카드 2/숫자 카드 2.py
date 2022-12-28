# 10816 숫자카드2 
import sys
from collections import Counter

num = int(input())
cards = sorted(list(map(int , sys.stdin.readline().split())))
exam_num = int(input())
exams = list(map(int, sys.stdin.readline().split()))

card_count = Counter(cards)

for i in range(exam_num):
    if exams[i] in card_count:
        print(card_count[exams[i]] , end = ' ')
    else:
        print(0 , end = ' ')