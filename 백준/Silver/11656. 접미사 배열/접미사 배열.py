# 11656 접미사 배열 

def make_jup_arr(s):
    jup_arr = []
    for i in range(len(s)):
        jup_arr.append(s[i:])
    return jup_arr

string = input()

arr = make_jup_arr(string)
arr.sort()
# print(arr)

for i in arr:
    print(i)

