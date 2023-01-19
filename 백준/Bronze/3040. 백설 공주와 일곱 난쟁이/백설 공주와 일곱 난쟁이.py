njy = []
for i in range(9):
    x = int(input())
    njy.append(x)

for i in range(9):
    for j in range(i + 1 , 9):
        if sum(njy) - (njy[i] + njy[j]) == 100:
            a = njy[i]
            b = njy[j]
njy.remove(a)
njy.remove(b)
for c in njy:
    print(c)