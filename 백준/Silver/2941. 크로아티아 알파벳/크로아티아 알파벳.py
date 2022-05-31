# 백준 2941번 
c_list = ['c=' , "c-" , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=' ]
# ljes=njak => 6


a = input()
for i in c_list: # 크로아티아 문자를 인덱싱 
    a = a.replace(i , "*") # 바꿔서 정리 

print(len(a)) # 정리한걸 셈 


