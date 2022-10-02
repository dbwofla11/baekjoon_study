# 2920
dma = list(map(int,input().split(" ")))
check_cnt = 0
for i in range(len(dma)):
  if i == 7:
    if dma[i-1] > dma[i]:
      check_cnt = check_cnt + 1
    elif dma[i-1] < dma[i]:
      check_cnt = check_cnt - 1
  else:
    if dma[i] > dma[i+1]:
      check_cnt = check_cnt + 1
    elif dma[i] < dma[i+1]:
      check_cnt = check_cnt - 1

if check_cnt == 8:
  print("descending")
elif check_cnt == -8:
  print("ascending")
else:
  print("mixed")