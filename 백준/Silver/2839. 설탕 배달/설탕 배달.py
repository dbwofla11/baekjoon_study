n = int(input())

cnt = 0

while True:
    if n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            break

        n -= 3
        cnt += 1
    else:
        cnt = -1
        break
    
print(cnt)
