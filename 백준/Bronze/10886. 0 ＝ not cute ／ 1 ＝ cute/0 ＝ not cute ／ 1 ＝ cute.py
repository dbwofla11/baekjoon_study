n = int(input())

zerocnt = 0
onecnt = 0

for i in range(n):
    zeroorone = int(input())
    if zeroorone == 1:
        onecnt += 1
    elif zeroorone == 0:
        zerocnt += 1
    else:
        pass

if onecnt > zerocnt:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")