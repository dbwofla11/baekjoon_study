nb = []
x = input()
for i in x:
    nb.append(i)
nb.sort(reverse=True)
for g in nb:
    print(g , end='')