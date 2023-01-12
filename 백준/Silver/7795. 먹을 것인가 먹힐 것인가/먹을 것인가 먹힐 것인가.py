# 7795 먹을 것인가 먹힐 것인가 
test_case = int(input())

def judge_hamsu(y , k): # x , k
    L , R = 0 , len(y) - 1
    res = -1
    while L <= R: 
        m = ( L + R ) // 2
        if y[m] < k:
            res = m 
            L = m + 1
        else:
            R = m - 1
    return res

    
for i in range(test_case):
    N , M = map(int , input().split())
    X = sorted(list(map(int , input().split())))
    y = sorted(list(map(int , input().split())))

    cnt = 0
    for x in X:
        cnt += judge_hamsu(y , x) + 1
        # print(cnt)
    print(cnt)