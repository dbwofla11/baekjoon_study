a = list(map(int, input().split(" ")))
for i in range(len(a)):
    idx = i
    for k in range(i+1 , len(a)):
        if a[idx] > a[k]:
            a[idx] , a[k] = a[k] , a[idx]

print(a[0],a[1],a[2])
