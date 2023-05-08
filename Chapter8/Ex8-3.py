N = int(input())
N_list = list(map(int, input().split()))

print(N, N_list)

dp = [0] * N
dp[-1] = N_list[-1]
dp[-2] = N_list[-2]

for i in range (N-3, -1, -1) :
    dp[i] = dp[i+2] + N_list[i]
print(max(dp))