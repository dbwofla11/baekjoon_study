# 4375 1 
# 11111111

# return 은 함수를 반환하지 while 무한루프를 막을 수 없다 

def basu(number):  
   
    one_temp = '1'  
    result_answer = 0

    while True:
        if int(one_temp) % number == 0:
            result_answer = len(one_temp)
            break
        else:
            one_temp += '1'

    return result_answer


while True:
    try:
        num = int(input())
        print(basu(num))
    except:
        break