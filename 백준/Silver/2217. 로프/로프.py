# 2217 로프 
import sys

N = int(sys.stdin.readline())

rope = []
w = []

for i in range(N):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True) # 1 1 1 1 1 1 1 1 10000 일 경우 생각 
for i in range(N):
    w.append(rope[i] * (i + 1)) # 동아줄의 수(N) * 최소 중량 
    # 10 15 40 -> 40 ~ 30  

print(max(w))

