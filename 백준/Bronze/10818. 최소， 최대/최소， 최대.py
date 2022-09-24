max = -1_000_000
min = 1000000
n = input()
nums = list(map(int,input().split(" ")))
 
for i in nums:
  if i <= min:
    min = i 

for a in nums:
  if a >= max:
    max = a

print(min, max)

