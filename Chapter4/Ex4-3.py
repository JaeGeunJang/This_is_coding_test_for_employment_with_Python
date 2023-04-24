move_correct = [[2, 1], [1, 2], [-1, 2],[-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
position_input = input()
position = [ord(position_input[0])-96, int(position_input[1])]

answer = 0
for moving in move_correct :
    if 0 < position[0] + moving[0] < 9 and 0 < position[1] + moving[1] < 9 :
        answer += 1
print(answer)