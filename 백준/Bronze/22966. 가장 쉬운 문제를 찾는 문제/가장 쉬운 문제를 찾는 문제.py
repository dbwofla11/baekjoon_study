#22966
list22966 = []

num_22966 = int(input())
for i in range(num_22966):
    a22966 , b22966 = map(str , input().split(" "))
    list22966.append([a22966 , int(b22966)])

answer22966 = sorted(list22966 , key = lambda x : x[1] )
print(answer22966[0][0])

