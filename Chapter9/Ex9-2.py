N, M, C = map(int, input().split())
inf = float('inf')

node = [[] for _ in range (N+1)]
distance = [inf for _ in range (N+1)]
visited = [False for _ in range (N+1)]

for _ in range (M) :
    X, Y, Z = map(int, input().split())
    node[X].append([Y, Z])

start = C
distance[start] = 0

def find_shortest() :
    next_start = start
    next_dist = inf

    for i in range (1, N+1) :
        if not visited[i] and next_dist > distance[i] :
            next_start = i
            next_dist = distance[i]
    return next_start

for _ in range (N) :
    for i in node[start] :
        if distance[i[0]] > distance[start] + i[1] :
            distance[i[0]] = distance[start] + i[1]
    visited[start] = True
    start = find_shortest()

canreach = 0
longest = 0

for i in distance :
    if i != inf and i != 0 :
        if longest < i :
            longest = i
        canreach += 1
print(canreach, longest)