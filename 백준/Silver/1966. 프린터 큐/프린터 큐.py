# 1966 프린터 큐 
from collections import deque

qu = deque()

for i in range(int(input())):
    
    n , m = map(int , input().split()) # n은 길이 , m은 몇번째로 뽑히는지 알고 싶은 숫자 
    qu = deque(map(int , input().split())) # 1 2 3 4
    # print(qu)
    # for num in qu_list:
    #     qu.append(num)

    cnt = 0 # 몇 번째로 출력 하는지 cnt 

    while qu:
        qu_max = max(qu)
        m -= 1 # 우리가 알고싶은 수가 한칸씩 왼쪽으로 이동 
        pop = qu.popleft()
        # print(qu)
        if qu_max != pop:
            qu.append(pop)
            if m < 0:
                m = len(qu) - 1 # 큐의 맨뒤의 인덱스 (우리가 알고싶은 수)

        else:
            cnt += 1 # 중요도가 제일 큰 것이 pop되었을 때 
            if m == -1: # 빠져 나왔을때 (우리가 알고싶은 수)
                print(cnt)
                break


