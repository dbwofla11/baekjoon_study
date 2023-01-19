a=list(range(1,31)); b = []; 
for i in range(28):
    b.append(int(input()))
c = set(a) - set(b)
print(min(c))
print(max(c))