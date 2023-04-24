N, M, K = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

result = 0
count = 0

for i in range(M) :
    if count < K :
        result += num_list[-1]
        count += 1
    else :
        result += num_list[-2]
        count = 0
print(result)