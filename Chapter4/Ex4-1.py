direction = {'U' : [-1, 0],'D' : [1, 0], 'L' : [0, -1], 'R' : [0, 1]}
N = int(input())

position = [1, 1]
input_dir = input().split()

for direct in input_dir :
    next = [position[0] + direction[direct][0], position[1] + direction[direct][1]]
    if 0 < next[0] < N and 0 < next[1] < N :
        position = next 

print(position[0], position[1])