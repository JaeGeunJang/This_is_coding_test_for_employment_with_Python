result = 0
N, K = map(int, input().split())

while N != 1 :
    if N % K != 0 :
        N -= 1
    else :
        N //= K
    result += 1
print(result)
