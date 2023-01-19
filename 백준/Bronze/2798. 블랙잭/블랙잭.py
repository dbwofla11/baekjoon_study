n , m = map(int , input().split(' '))
x = list(map(int , input().split(' ')))
max = 0
for i in range(n - 2):
    for j in range(i + 1 , n - 1 ):
        for k in range(j + 1 , n):
            if x[i] + x[j] + x[k] <= m:
                if max <= x[i] + x[j] + x[k]:
                    max = x[i] + x[j] + x[k]
print(max)