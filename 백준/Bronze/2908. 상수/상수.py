a , b = input().split()
a1 = int(a[::-1])
b1 = int(b[::-1])
if a1 >= b1:
  print(a1)
else:
  print(b1)