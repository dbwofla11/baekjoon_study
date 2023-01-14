nb = ['0','1','2','3','4','5','6','7','8','9']

a = int(input())
b = int(input())
c = int(input())

x = a * b * c
x = str(x)

for i in nb:
    print(x.count(i))