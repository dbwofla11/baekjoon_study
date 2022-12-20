x = int(input())
z1 = 0
z2 = 0
z3 = 0
z4 = 0
AXIS = 0
for i in range(x):
    a , b = map(int , input().split(" "))
    if a == 0 or b == 0:
        AXIS = AXIS + 1 
    else:
        if a > 0 and b > 0:
            z1 = z1 + 1
        if a < 0 and b > 0:
            z2 = z2 + 1
        if a < 0 and b < 0:
            z3 = z3 + 1
        if a > 0 and b < 0:
            z4 = z4 + 1
print("Q1: {}".format(z1))
print("Q2: {}".format(z2))
print("Q3: {}".format(z3))
print("Q4: {}".format(z4))
print("AXIS: {}".format(AXIS))