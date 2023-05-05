# First 11min 57sec

N = int(input())
coin_list = sorted(list(map(int, input().split())))
coin_list.reverse()

tmp = 1
while True :
    answer = tmp
    for i in coin_list :
        if answer >= i :
            answer -= i
    if answer == 0 :
        tmp += 1
    else :
        print(tmp)
        break