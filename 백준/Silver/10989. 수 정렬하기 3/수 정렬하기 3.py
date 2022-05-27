import sys
n = int(sys.stdin.readline()) # 맨 처음 숫자  # 더 빠르게 하기 위해 sys.stdin 이용함
sub = [0] * 10001 # 메모리 활당 -> 모든 배열이 0으로 채워짐 

for _ in range(n):
    num = int(sys.stdin.readline()) # 빠르게 입력받기 인덱스에 표시만 해줌 
    sub[num] = sub[num] + 1  # 표시된 인덱스에 1을 넣어줌 
    


for i in range(10001):    #체크배열을 10001번 반복 
    if sub[i] != 0 :    # 배열값이 0이 아니거나 다른 숫자면
        for _ in range(sub[i]):  # 인덱스에 표시해주었으니 숫자를 반환함 배열에 들어가는 숫자가 1~10000까지니 
            print(i) # 그 값만큼 반환함

            #이런 체크 방식을 n번 반복함 