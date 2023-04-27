N, M = map(int, input().split())

ice = []
result = 0

for i in range(N) :
    ice.append(list(map(int, input())))

def dfs(ice, N1, M1) :
    if not (0 <= N1 < N) or not(0 <= M1 < M) :
        return False
    if ice[N1][M1] == 0 :
        ice[N1][M1] = 1
        dfs(ice, N1+1, M1)
        dfs(ice, N1-1, M1)
        dfs(ice, N1, M1+1)
        dfs(ice, N1, M1-1)

for n in range (N) :
    for m in range (M) :
        if ice[n][m] == 1 :
            continue
        else :
            dfs(ice, n, m)
            result += 1
print(result)
