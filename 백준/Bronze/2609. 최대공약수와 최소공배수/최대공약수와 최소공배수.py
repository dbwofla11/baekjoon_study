# 최대공약수 , 최대 공배수 

n1 , n2 = map(int,input().split(" "))
def gcd(n1 , n2):
  if n1 == 0:
    return n2
  else: return gcd(n2%n1 , n1)

def gcp(n1 , n2):
  return (n1 * n2) / gcd(n1,n2)

print(gcd(n1,n2))
print(int(gcp(n1,n2)))


