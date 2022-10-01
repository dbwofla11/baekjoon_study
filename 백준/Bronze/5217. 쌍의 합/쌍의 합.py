 # 5217
cnt = int(input())
for i in range(cnt):
  num = int(input())
  if num <= 2:
    print(f'Pairs for {num}:')
  else:
    print(f'Pairs for {num}:' ,end=" ") # 3 -> 1,2
    for k in range(1,(num + 1)//2 ):
      if k == (num + 1)//2 - 1:
        print(f'{k} {num - k}')
      else:
        print( f'{k} {num - k},' , end = " ")