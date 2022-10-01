x = int(input()) # 5 
for i in range(x):
    for k in range(x - i - 1): # 4
        print(" " , end="")
    for s in range(i + 1):
        print("*" , end="")
    print("")

    