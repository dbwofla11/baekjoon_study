# 정수를 나타내는 방법 

def func(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else: # 여태까지의 조합 1 ,2 ,3의 정수를 나타내는 방법을 조합해서 다시 쓸수 있음 
    return func(n-1) + func(n - 2) + func(n - 3) # ex 4면 1,2,3의 케이스를 조합해서 리턴함 
  
# 이럼 경우의 수가 나옴 
case = int(input())
for _ in range(case):
  num = int(input())
  result = func(num)
  print(result)
