Au = []
for orange in range(10):
    x = int(input())
    v = x%42
    Au.append(v)

Au = set(Au)
print(len(Au))