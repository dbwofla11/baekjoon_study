ejdcl = []
n = int(input())
for i in range(n):
    x , y = map(int , input().split(' '))
    ejdcl.append([x , y])

rank = []
for k in range(n):
    cnt = 0
    for j in range(n): 
        if ejdcl[k][0] < ejdcl[j][0] and ejdcl[k][1] < ejdcl[j][1]:
            cnt += 1
    rank.append(cnt + 1)

print(*rank)