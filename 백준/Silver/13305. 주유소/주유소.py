# 13305 주유소 
# 제일 싼 주유소에 도착 전까지 현재 주유소에서 다음 도시로 이동할 만큼만 넣기 

city_num = int(input())

road = list(map(int , input().split())) # 2 3 1 
oil_cost = list(map(int , input().split())) # 5 2 4 1 

arr = []
result = 0 

for i in range(len(oil_cost) - 1):
    arr.append(oil_cost[i])

min_num = min(arr)
min_i = arr.index(min_num)

# print(min , min_i)
for i in range(0 , min_i):
    # print(oil_cost[i] * road[i])
    result += oil_cost[i] * road[i]

for i in range(min_i , len(road)):
    result += oil_cost[min_i] * road[i]

print(result)

