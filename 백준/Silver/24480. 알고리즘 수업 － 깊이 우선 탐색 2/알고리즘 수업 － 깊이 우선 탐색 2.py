# 24480 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(10**6)

N , M , R = map(int , input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

for _ in range(M):
    s , e =  map(int, sys.stdin.readline().split()) # 시작 포인트 , 엔드 포인트 sys.stdin.readline
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort(reverse=True)

def dfs(graph , v , visited):
    
    global cnt
    visited[v] = cnt
    cnt += 1
        
    # print(v , end='\n')

    for i in graph[v]:
        if visited[i] == 0: # not visited --> 이렇게 bool 형으로 하면 False , True로 박에 안나옴 visited[i] == 0
            dfs(graph , i , visited)

dfs(graph , R  , visited)
for i in visited[1:]:
    print(i)
