# First 9min 1sec

N, M = map(int, input().split())
total_M = [0] * (M+1)

for i in list(map(int, input().split())) :
    total_M[i] += 1

answer = 0

for i in range (1, M) :
    for j in range (i+1, M+1) :
        answer += total_M[i] * total_M[j]

print(answer)