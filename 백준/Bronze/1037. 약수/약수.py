# 1037 약수 

num = int(input())
numbers = list(map(int , input().split()))
print(max(numbers) * min(numbers))