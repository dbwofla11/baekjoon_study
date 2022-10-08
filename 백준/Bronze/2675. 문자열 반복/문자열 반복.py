s = int(input())
for i in range(s):
  x , y = input().split(" ")
  x = int(x)
  for k in y:
    print(k*x ,end="")
  print('')