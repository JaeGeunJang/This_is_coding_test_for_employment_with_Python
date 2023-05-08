M = int(input())
dp = [0] * 30001

for i in range (2, M+1) :
    tmp = [dp[i-1]]
    if i%5 == 0 :
        tmp.append(dp[i//5])
    elif i%3 == 0 :
        tmp.append(dp[i//3])
    elif i%2 == 0 :
        tmp.append(dp[i//2])
    dp[i] = min(tmp) + 1
print(dp[M])