from collections import deque

qu = deque()
answer = []

n , k = map(int,input().split())

for i in range(1, n+1):
    qu.append(i)

while qu:
    for i in range(k-1):
        qu.append(qu.popleft()) # 그냥 통과 , 앞으로 나갔던게 뒤로 돌아오니까 회전하는 역활도 함 
    answer.append(qu.popleft()) # 회전 큐는 앞으로 나간게 뒤로 돌아온다는 특징이 있음 

# print(*answer)
print('<' , end = "")
for i in range(n-1):
    print("{},".format(answer[i]) , end=" ")
print(answer[-1] , end=">")