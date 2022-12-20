arr=[]
for i in range(9):
    arr.append(int(input()))

for i in range(9):
    for j in range(9):
        if sum(arr)-arr[i]-arr[j]==100:
            x,y=i,j
            break
            
arr.remove(arr[x])
arr.remove(arr[y])
arr.sort()
for i in arr:
    print(i)