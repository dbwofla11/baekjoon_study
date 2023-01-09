# 5648 역원소 정렬 
# import sys 

# nums = list(map(int , input().split(" ")))

element = []
n , index = 2000000000 , 0 
while True:
    if len(element) == n:
        break
    tmp_i = 0
    for i in list(map(int , input().split())):
        if index == 0 and tmp_i == 0:
            n = i
            index = 1
        else:
            element.append(int(''.join(reversed(str(i)))))

element.sort()
for i in element:
    print(i)

