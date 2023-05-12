# first : 36min 47s
# site : https://www.acmicpc.net/problem/18405

from collections import deque

N, M = map(int, input().split())
mini_map = []
sort_list = []

for i in range (N) :
    a = list(map(int, input().split()))
    for j in range (len(a)) :
        if a[j] != 0 :
            sort_list.append((a[j], i, j))
    mini_map.append(a)
sort_list.sort()
sort_list = deque(sort_list)
S, X, Y = map(int, input().split())

def virus (graph, y, x, v) :
    direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    return_list = []
    for dir in direct :
        newy, newx = y+dir[0], x+dir[1]
        if (0 <= newy < N) and (0 <= newx < N) :
            if graph[newy][newx] == 0 :
                graph[newy][newx] = v
                return_list.append([v, newy, newx])
                # virus(graph, newy, newx, v)
    return return_list

for times in range(S) :
    new_queue = deque()
    while sort_list :
        s_list = sort_list.popleft()
        a = virus(mini_map, s_list[1], s_list[2], s_list[0])
        for aa in a :
            new_queue.append(aa)
    sort_list = new_queue
    
print(mini_map[X-1][Y-1])