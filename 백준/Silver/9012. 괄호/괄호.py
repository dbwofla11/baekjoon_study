# 9012 괄호 

# VPS => 예를 들어 “(())()”와 “((()))”  # “(()” 는 모두 VPS 가 아닌 문자열이다. 
# '(' 랑 ')' 의 카운트가 같으면 yes , 다르면 no 
# 
n = int(input())

for i in range(n):
    
    string = input()

    stack = []
    L_cnt , R_cnt = 0 , 0 
    
    for string_word in string:
        if string_word == '(':
            L_cnt += 1
            stack.append('(')
        elif string_word == ')':
            if len(stack) == 0:
                R_cnt += 1 
            else:
                R_cnt += 1
                stack.pop()
    
    if len(stack) == 0 and R_cnt == L_cnt:
        print("YES")
    else:
        print("NO")