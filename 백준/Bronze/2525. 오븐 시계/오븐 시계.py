A , B = input().split(" ")
C = int(input()) # 더하는 시간 80분 
A = int(A) # 시 
B = int(B) # 분 

h1 = C//60 # 1시간  
m1 = C%60 # 20분 

m = B + m1 # 일단 더해줌 
h2 = A + h1 + m//60

h = h2%24
print(h , m%60)