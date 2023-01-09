# # 백준 1431
# A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

num = int(input())
silial = []

def sum_num(x):
    sum = 0
    for i in x:
        if i.isdigit(): # 숫자인지 판별하고 자리수 더하기 
            sum += int(i)
    return sum


for i in range(num):
    silial.append(input())

silial.sort( key = lambda x : (len(x) , sum_num(x) , x))
for i in silial:
    print(i)
