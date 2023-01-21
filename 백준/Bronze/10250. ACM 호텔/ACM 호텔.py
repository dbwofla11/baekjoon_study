# 10250 ACM호텔 
num = int(input())

for i in range(num):
    H , W , N = map(int , input().split())
    people_h , people_w = 0 , 0

    if N % H == 0:
        people_h = H * 100
        people_w = N // H
        print( people_h + people_w )
    else:
        people_h = (N % H) * 100
        people_w = N // H + 1
        print( people_h + people_w )

