# First : 13min 24sec

N = list(map(int, input()))
answer = [0, 0]
now = -1

for i in N :
    if now != i :
        answer[i] += 1
        now = i
print(min(answer))