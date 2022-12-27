# 26215 눈 치우기 - < 문제가 이상함 > 
num = int(input())
snows = list(map(int , input().split()))

snows.sort()

# print(top_snow_kg)
time = 0 

# if num == 1:
#     if snows[0] > 1440: print(-1)
#     else: print(snows[0])


while True:

    if num == 1:
        if snows[0] > 1440: 
            time = -1
            break
        else:
            time = snows[0]
            break

    snows.sort()
    if snows[num -1] == 0 : break
    
    snows[num - 1] -= 1
    if snows[num -2] != 0 : 
        snows[num -2] -= 1
    time += 1
    

    if time > 1440:
        time = -1
        break
    

print(time)