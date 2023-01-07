h = []

for i in range(9):
    a = int(input())
    h.append(a)

for i in range(9):
    for s in range(i + 1 , 9):
        if sum(h) - (h[i] + h[s]) == 100:
            x1 = h[i]
            y1 = h[s]

h.remove(x1)
h.remove(y1)

print('\n'.join(map(str, sorted(h))))