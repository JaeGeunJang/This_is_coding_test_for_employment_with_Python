Time = [0, 0, 0]
N = int(input())

answer = 0

while Time[0] <= N :
    Time[2] += 1
    if '3' in str(Time[0]) or '3' in str(Time[1]) or '3' in str(Time[2]) :
        answer += 1

    if Time[2] == 60 :
        Time[2] = 0
        Time[1] += 1
    if Time[1] == 60 :
        Time[1] = 0
        Time[0] += 1
        
print(answer)