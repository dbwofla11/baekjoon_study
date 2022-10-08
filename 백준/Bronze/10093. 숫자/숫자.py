a , b = map(int,input().split(" ")) 
if a == b:
    print(0)
else:
    maaaax = max(a , b)
    miiiin = min(a , b)

    print(maaaax - miiiin - 1)
    for l in range(miiiin + 1 , maaaax):
        print(l , end = " ")