lst = list(map(int, input().split(" ")))
cnt = 0
for i in range(len(lst)):
  if i == 7:
    if lst[i-1] < lst[i]:
      cnt += 1
    elif lst[i-1] > lst[i]:
      cnt -= 1
    else:
      cnt = 0
  else:
    if lst[i] < lst[i+1]:
      cnt += 1
    elif lst[i] > lst[i+1]:
      cnt -= 1
    else:
      cnt = 0

if cnt == 8:
  print('ascending')
elif cnt == -8:
  print('descending')
else:
  print("mixed")