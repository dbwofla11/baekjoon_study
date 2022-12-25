import sys
num = int(input())

time = []
for i in range(num):
    a , b = map(int, sys.stdin.readline().split(" "))
    time.append((a,b))

time.sort(key= lambda x : (x[1] , x[0]))

#LIS 알고리즘 
cnt = 1 
end_time = time[0][1] # 처음거 
for i in range(1 , num):
    if time[i][0] >= end_time: # end_time이 뒤에꺼 time[i][0] 이 앞에꺼로 해서 LIS적용 
        cnt += 1
        end_time = time[i][1]  #(0 10) (3 4) (2 3) (1 2) # 엔드타임 갱신 1 -> 2 -> 3 -> 4 이런식으로 

print(cnt)
