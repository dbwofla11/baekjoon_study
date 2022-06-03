import sys 
input = sys.stdin.readline

num = int(input()) 
a = []

for i in range(num):
  a.append(int(input()))

a = sorted(a , reverse=True)

for i in a: 
  print(i)
  
  
  
