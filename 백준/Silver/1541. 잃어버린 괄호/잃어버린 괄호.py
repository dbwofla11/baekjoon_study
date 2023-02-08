# 1541 잃어버린 괄호 , 가장 처음과 마지막 문자는 숫자이다.

A = input().split("-") # 55-50+40 -> 55 , 50+40

nums = []
for i in A:
    m = 0
    B = i.split("+")
    for k in B:
        m += int(k)
    nums.append(m)

num = nums[0]
for i in range(1,len(nums)):
    num -= nums[i]

print(num)