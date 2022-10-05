num = int(input())
# num은 3의 거듭제곱수  
# ex num은 3가정  

def star(num):
  if (num == 1):
    return ["*"]
  else:
    s = star(num//3) # 감소 num을 1까지 만들게 함  # 이렇게 하면 마지막 num이 1일때의 함수가 s에 *을 리턴해서 대입함 
    pracktal = []
    for i in s:
      pracktal.append(i*3)
    for i in s:
      pracktal.append(i + " "*(num//3) + i) # 코드의 일치성 
    for i in s:
      pracktal.append(i*3)
    return pracktal

stars = star(num)
print('\n'.join(stars))