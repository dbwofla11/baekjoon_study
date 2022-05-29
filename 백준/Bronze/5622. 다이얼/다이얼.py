#백준 5622

numlst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] # ex ) index WXYZ de W , ABC de A 

lst = list(input())
time = 0

for i in lst: # [W, A] 
    for k in numlst:
        if i in k :
            time += numlst.index(k) + 3

print(time)