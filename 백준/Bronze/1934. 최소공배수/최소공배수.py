
def gcd(a,b):
    if(b == 0): return a
    else: return gcd(b , a%b) # 12 

def uc(a,b):
    r = (a*b) // gcd(a , b) # 
    return r

num1934 = int(input())
for i in range(num1934):
    a1934 , b1934 = map(int, input().split(" "))
    print(uc(a1934 , b1934))