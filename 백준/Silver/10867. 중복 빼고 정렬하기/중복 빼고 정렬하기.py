# 10867 중복 빼고 정렬하기

num = int(input())
num_list = sorted(set(map(int , input().split())))

for i in num_list:
    print(i , end = ' ')
