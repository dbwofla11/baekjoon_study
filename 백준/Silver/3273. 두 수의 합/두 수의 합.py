
x = int(input())
y = list(map(int , input().split(' ')))
z = int(input())

cnt = 0
for i in y:
    if z - i in y:
        cnt += 1

print(cnt // 2)