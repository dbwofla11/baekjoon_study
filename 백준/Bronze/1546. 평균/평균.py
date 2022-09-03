Nn = int(input())
lemon = []
orange = list(map(int, input().split()))

orange.sort()
Mm = orange[-1] 
# print("MAX is", Mm) [80,40,60] max = 80 
# 80/80*100 , 40/80*100 , 60/80*100 => 평균 
for i in orange:
    b = i/Mm*100
    lemon.append(b)

avg = sum(lemon, 0.0)/len(lemon)
print(avg)
