# 24479 알고리즘 수업 - 깊이 우선 탐색 1 
import sys
sys.setrecursionlimit(10**9)


def dfs(graph , v , visited):
    
    global cnt
    visited[v] = cnt
    cnt += 1
        
    # print(v , end='\n')

    for i in graph[v]:
        if visited[i] == 0: # not visited --> 이렇게 bool 형으로 하면 False , True로 박에 안나옴 visited[i] == 0
            dfs(graph , i , visited)

N , M , R = map(int , input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

for _ in range(M):
    s , e =  map(int, sys.stdin.readline().split()) # 시작 포인트 , 엔드 포인트 sys.stdin.readline
    graph[s].append(e)
    graph[e].append(s)


# print(graph)

for i in graph:
    i.sort()

dfs(graph , R , visited)
for i in range(1 , N+1):
    print(visited[i])



