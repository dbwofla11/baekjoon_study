n = int(input())
for k in range(n):
    ox = input()
    s = list(ox.split("X"))
    cnt = 0
    for i in s:
        answer = (len(i)*(len(i)+1))/2
        cnt += answer

    print(int(cnt))