# first : Fail
# Site : https://www.acmicpc.net/problem/14502

from itertools import permutations
from copy import deepcopy
N, M = map(int, input().split())
mini_map = []

for _ in range(N) :
    mini_map.append(list(map(int, input().split())))

wall_where = list(permutations(range(N*M), 3))

def virus(maping, y, x) :
    axis = [[0, 1],[1, 0], [-1, 0], [0, -1]]
    for i in axis :
        newx = x+i[1]
        newy = y+i[0]
        if (0 <= newx < M) and (0 <= newy < N) :
            if maping[newy][newx] == 0 :
                maping[newy][newx] = 2
                virus(maping, newy, newx)
        
max_num = 0

for i in wall_where :
    for k in i :
        new_map = deepcopy(mini_map)
        
        if new_map[k//M][k%M] == 0 :
            new_map[k//M][k%M] = 1

    for n in range (N) :
        for m in range (M) :
            if new_map[n][m] == 2 :
                virus(new_map, n, m)
    # print(new_map)
    tmp = 0
    for n in range (N) :
        for m in range(M) :
            if new_map[n][m] == 0 :
                tmp += 1
    
    for aaa in new_map :
        print(aaa)
    print()
    if max_num < tmp :
        max_num = tmp
        
print(max_num)
