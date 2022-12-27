# 10815 숫자카드 
import sys

num = int(input())
cards = sorted(list(map(int , sys.stdin.readline().split())))
exam_num = int(input())
exams = list(map(int, sys.stdin.readline().split()))

for exam in exams:
    left , right = 0 , num - 1
    exist = False

    while left <= right:
        
        mid = ( left + right ) // 2

        if cards[mid] > exam: # 상근의 카드가 제시된거 보다 높을 때 
            right = mid - 1
        elif cards[mid] < exam: # 낮을 떄 
            left = mid + 1
        else:
            exist = True
            break
    
    if exist: print(1)
    else: print(0)

