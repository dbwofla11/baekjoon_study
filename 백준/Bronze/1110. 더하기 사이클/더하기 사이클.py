cnt = 0
num = int(input())
n = num

while True:
    cnt += 1
    new = (n // 10) + (n % 10)
    n = (n % 10) * 10 + (new % 10)
    if num == n:
        break

print(cnt)