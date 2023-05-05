# First : 3min 0sec

answer = 0
plus = False

num_list = list(map(int, input()))
num_list.sort()

for i in num_list :
    if not plus :
        if i != 0 :
            answer += i
            plus = True
    else :
        answer *= i

print(answer)