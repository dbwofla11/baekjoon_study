a = list(map(int,input().split(" ")))

for i in range(len(a)): #5번 반복 
  idx = i #  12345 index
  for k in range(i + 1 , len(a)): # 시간을 줄인다 
    if a[idx] > a[k]:
      a[idx] , a[k] = a[k] , a[idx]

print(a[0] , a[1] , a[2])
                 