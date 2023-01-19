# 3986 좋은 단어 
num = int(input())
cnt = 0

for i in range(num):
    string = input()
    stack = []

    for t in string:
        # print("t:" , t)
        if not stack:
            stack.append(t)
        elif stack[-1] == t:
            stack.pop()
            # print(stack)
        else:
            stack.append(t)

    if len(stack) == 0:
        cnt += 1


print(cnt)
