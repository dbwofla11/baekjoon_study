a , b = map(int, input().split(" "))
if a == b:
  print(0)
else:
  m = max(a,b) # 최대범위
  n = min(a,b) # 최소범위  # (8 , 14) 9 ~ 13 안포함  # [8 ,14] 8 ~ 14 포함된거 
  box = m - n - 1 # [1 , 10)
  print(box)
  for i in range(n +1 , m):
    print(i , end =' ')