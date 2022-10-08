# 반복문 
n = int(input())
def fibo(n):
  a , b = 1 ,1
  if n == 1 or n == 2:
    return 1
  for i in range(1, n):
    a , b = b , a+b

  return a

avg = fibo(n)
print(avg) # 1, 1 , 2 , 3 , 5 ,8