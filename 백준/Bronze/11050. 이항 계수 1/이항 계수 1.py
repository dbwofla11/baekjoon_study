# 이항계수 구하기 
# 조합구하기 
def fact(n):
  if n <= 1 :
    return 1
  else : return fact(n-1) * n

n , r = map(int,input().split(" "))
print( fact(n) // (fact(r) * fact(n - r) ))