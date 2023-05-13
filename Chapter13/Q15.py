# first : 29:05

N, M, K, X = map(int, input().split())

total_map = [[] for _ in range (N+1)]
visited = [False for _ in range (N+1)]
for i in range (M) : 
    A, B = map(int, input().split())
    total_map[A].append(B)

distance = [0 for _ in range (N+1)]

from collections import deque

def bfs (graph, start, visited) :
    queue = deque([start])
    visited[start] = True 

    while queue :
        v = queue.popleft()

        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
bfs(total_map, X, visited)
if K not in distance :
    print(-1)
else :
    for i in range(1, N+1) :
        if distance[i] == K :
            print(i)