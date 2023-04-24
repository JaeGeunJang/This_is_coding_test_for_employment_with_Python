M = int(input())
coin_list = [500, 100, 50, 10]
change = [0 for _ in range(len(coin_list))]

while M >= coin_list[-1] :
    for i in range(len(coin_list)) :
        coin_num = M//coin_list[i]
        change[i] += coin_num
        M -= coin_num * coin_list[i]
print(change)
