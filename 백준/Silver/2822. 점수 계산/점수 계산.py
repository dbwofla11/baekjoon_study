n2822 = []
for i in range(8):
    n2822.append(int(input()))

temp2822 = sorted(n2822 , reverse=True)
sum2822 = temp2822[0] + temp2822[1] + temp2822[2] + temp2822[3] + temp2822[4]

print(sum2822)

index_temp2822 = []
for i in range(5):
    ans2822 = n2822.index(temp2822[i])
    index_temp2822.append(ans2822)

index_temp2822.sort()
for i in range(5):
    print(index_temp2822[i] + 1 , end=" ")