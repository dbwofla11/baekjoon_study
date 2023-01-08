# 수 정렬하기 5
import sys
s = []
for i in range(int(input())):
    s.append(int(sys.stdin.readline()))
for i in sorted(s):
    print(i)
