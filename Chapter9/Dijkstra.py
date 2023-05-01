'''
input

node, weight : 6 11
start : 1

start, end, distance
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

inf = float('inf')

N, W = map(int, input().split())
start = int(input())

Nodes = [[] for _ in range (N+1)]
min_dist = [inf for _ in range (N+1)]
visited = [False for _ in range (N+1)]

for i in range (W) :
    S, E, L = map(int, input().split())
    Nodes[S].append((E, L))
    
def find_min() :
    next_value = inf
    next_start = start
    for i in range (1, N+1) :
        if not visited[i] and next_value > min_dist[i] :
            next_value = min_dist[i]
            next_start = i
    return next_start

min_dist[start] = 0

for _ in range (N) :
    for i in Nodes[start] :
        if min_dist[start] + i[1] < min_dist[i[0]] :
            min_dist[i[0]] = min_dist[start] + i[1]
    visited[start] = True

    start = find_min()

print(min_dist)
