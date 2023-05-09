N, M = map(int, input().split())
N_list = list(map(int, input().split()))

start = 0
end = max(N_list)

result = 0

while True :
    mid = (start + end)//2
    if start > end :
        break
    sum = 0
    for n in N_list :
        if n > mid :
            sum += n-mid
    if sum >= M :
        result = sum
        start = mid + 1
    else :
        end = mid - 1
print(mid)