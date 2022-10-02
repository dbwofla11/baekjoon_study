# 나이순 정렬

n = int(input())
member = []

for i in range(n):
  age , name = input().split(" ")
  age = int(age)
  member.append([age , name]) # i는 들어온 순서
  # print("현재" , l)

member_name = [i[1] for i in member] # 이름 순서 
age = sorted(member , key = lambda i : i[0] )
for k in age:
  print(k[0] , k[1])


