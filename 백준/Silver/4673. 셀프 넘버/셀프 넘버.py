# 4673 셀프 넘버 
x = set(range(1 , 10001))
y = set()

for i in range(1 , 10001):
    for j in str(i):
        i += int(j)
    y.add(i)

z = sorted(x - y)
for s in z:
    print(s)