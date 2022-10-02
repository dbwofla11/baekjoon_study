# 2475 검증수 
a = list(map(int,input().split(" ")))
sum = 0
for i in a:
  sum = sum + int(i)**2 

answer = sum % 10
print(answer)