# 1018 체스판 다시 칠하기 

# 입력 
N , M = map(int , input().split())
board = list()
for i in range(N):
    board.append(input())

r = list()


# 고치기 # B만 바꾸는 경우와 W만 바꾸는 경우  
for a in range(N-7):
    for b in range(M-7):
        check_w = 0
        check_b = 0 
        for block_N in range(a , a+8):
            for block_M in range(b , b+8):
                if (block_M + block_N) % 2 == 0: ### b|bbb때 2번 인덱스가 w야지 체스판이 됨 
                    if board[block_N][block_M] != 'W':
                        check_w += 1
                    if board[block_N][block_M] != 'B':
                        check_b += 1
                else:
                    if board[block_N][block_M] != 'B':
                        check_w += 1
                    if board[block_N][block_M] != 'W':
                        check_b += 1
        r.append(check_b)
        r.append(check_w)

print(min(r))
 
