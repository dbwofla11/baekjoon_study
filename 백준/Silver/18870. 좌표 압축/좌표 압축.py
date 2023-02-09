# 18870 좌표 압축 

num = int(input())

x_list = list(map(int , input().split())) # 2 4 -10 4 -9 -> 2 3 0 3 1

element = sorted(list(set(x_list))) # -10 , -9 , 2 , 4
index_dic = {element[i] : i for i in range(len(element))}

# print(index_dic)
for i in x_list:
    # print("i",i)
    print(index_dic[i] , end = " ")