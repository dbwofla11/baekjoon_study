# 10825 국영수 
import sys
num = int(input())

score = []
for i in range(num):
    tmp = list(map(str , sys.stdin.readline().split()))
    score.append([tmp[0] , int(tmp[1]) , int(tmp[2]) , int(tmp[3]) ])

score.sort( key = lambda x : ( -x[1] , x[2] , -x[3] , x[0]))

for i in score:
    print(i[0])
