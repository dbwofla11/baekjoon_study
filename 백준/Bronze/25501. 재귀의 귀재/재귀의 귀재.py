
def recur(s , l , r  , cnt):
    if l >= r: return 1 , cnt
    elif s[l] != s[r]: return 0 , cnt # 얘는 됨  
    else: return recur(s , l+1 , r-1 , cnt+1)
n = int(input())

for i in range(n):
    s = input()
    r , cnt = recur(s , 0 , len(s)-1 , 0)
    print(r , cnt+1)