grade = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 
'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}

a , b , c = 0 , 0 , 0
def new_round(n):
    n *= 100
    if (n - int(n)) >= 0.5:
        return (int(n)+1)/100
    else: return int(n)/100 # 소수 둘째 자리 까지 반올림 


for i in range(int(input())):
    x , y , z = map(str , input().split())
    a += int(y) * grade[z]
    b += int(y)

print('{0:.2f}'.format(new_round(a / b)))
