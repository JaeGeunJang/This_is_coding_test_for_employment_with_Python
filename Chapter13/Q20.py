from itertools import combinations
from copy import deepcopy

N = int(input())

def check_student(map, y, x, direction, N) :
    if direction == 0 :
        while x >= 0 :
            if map[y][x] == 'O' :
                return True
            if map[y][x] == "S" :
                return False
            x -= 1
    elif direction == 1 :
        while x < N :
            if map[y][x] == 'O' :
                return True
            if map[y][x] == "S" :
                return False
            x += 1
    elif direction == 2 :
        while y >= 0 :
            if map[y][x] == 'O' :
                return True
            if map[y][x] == "S" :
                return False
            y -= 1
    elif direction == 3 :
        while y < N :
            if map[y][x] == 'O' :
                return True
            if map[y][x] == "S" :
                return False
            y += 1
    return True

teachers = []
student = []
blank = []
mini_map = []

for i in range (N) :
    lines = input().split()
    mini_map.append(lines)

    for line in range(N) :
        if lines[line] == 'S' :
            student.append([i, line])
        elif lines[line] == 'T' :
            teachers.append([i, line])
        else :
            blank.append([i, line])

blank_combi = combinations(blank, 3)

def total_check(mini_map, teachers, N) :
    for teach in teachers :
        for i in range (4) :
            check = check_student(mini_map, teach[0], teach[1], i, N)
            if not check :
                return False
    return True

result = False
for combi in blank_combi :
    for com in combi :
        mini_map[com[0]][com[1]] = 'O'
    if total_check(mini_map, teachers, N) :
        result = True
        break
    for com in combi :
        mini_map[com[0]][com[1]] = 'X'
    
if result :
    print("YES")
else :
    print("No")
    