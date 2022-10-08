s = int(input())
for i in range(s):
    a = ''
    n , answk = input().split(' ')
    n = int(n)
    for k in answk: # answk = abc a, b, c
        a += k * n
    print(a)  