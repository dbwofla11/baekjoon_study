lst = input()
new = lst.strip()
if new == '':
    print(0)
else:
    m = list(new.split(" "))
    print(len(m))