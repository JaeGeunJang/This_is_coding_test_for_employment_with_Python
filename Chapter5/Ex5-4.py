from collections import deque

N, M = map(int, input().split())

mini_map = []

for n in range (N) :
    mini_map.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


queue = deque()
queue.append([0, 0])

while queue :
    hello = queue.popleft()
    for i in range (4) :
        new_x, new_y = hello[0] + dx[i], hello[1] + dy[i]
        
        if not(0 <= new_x < M) or not(0 <= new_y < N) :
            continue
        if mini_map[new_y][new_x] == 0 :
            continue
        if mini_map[new_y][new_x] == 1 :
            queue.append([new_x, new_y])
            mini_map[new_y][new_x] += mini_map[hello[1]][hello[0]]

print(mini_map[N-1][M-1])