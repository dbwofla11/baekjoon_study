rank = [] 
for i in range(9):
    a = int(input())
    rank.append(a)

max = -9999999999999999999999999999999999999999999999999999999999999999999
for i in rank: # [4,2,3,1]
    if max < i:
        max = i
        
print(max)
print(rank.index(max) + 1)