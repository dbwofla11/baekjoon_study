n = int(input())

for i in range(n):
    a , b = input().split(" ")
    a = int(a)
    b = int(b)
    if a < b:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")