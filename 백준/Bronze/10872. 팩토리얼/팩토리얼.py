n = int(input())
fact = 1
if fact == 0:
    print(1)
else:
    for i in range(1,n+1):
        fact = fact * i
    print(fact )