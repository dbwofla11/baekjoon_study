#10093 숫자
a ,b = map(int,input().split(" "))
n1 = min(a,b)
n2 = max(a,b)
n = abs(n2 - n1 -1)# 범위 
if n1 == n2:
  n = 0
print(n)

for i in range(n1+1 , n2 , 1):
  print(i , end =" ")