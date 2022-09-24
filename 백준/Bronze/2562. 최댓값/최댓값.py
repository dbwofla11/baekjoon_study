a = []
max = 0


for i in range(9):
  q = int(input())
  a.append(q)

for i in a:
  if i >= max:
    max = i

print(max)
print(a.index(max) + 1)