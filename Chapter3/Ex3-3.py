N, M = map(int, input().split())
min_max = 0
for i in range (N) :
    min_num = min(list(map(int, input().split())))
    if min_max < min_num:
        min_max = min_num
print(min_max)