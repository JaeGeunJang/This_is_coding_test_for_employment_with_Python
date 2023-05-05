#First 23min 31sec

N = int(input())
manList = list(map(int, input().split()))

manList.sort()
result = 0

new_list = []

while True :
    if not new_list :
        new_list.append(manList[0])
        manList = manList[1:]

    if max(new_list) == len(new_list) :
        result += 1
        new_list = []

    else :
        if not manList :
            break
        else :
            new_list.append(manList[0])
            manList = manList[1:]

print(result)