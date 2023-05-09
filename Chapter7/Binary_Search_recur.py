def binary_search(array, target, start, end) :
    if start > end :
        return False
    
    mid = (start+end)//2
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    else :
        return binary_search(array, target, mid+1, end)
    
if __name__ == "__main__" :
    import random
    arr = [random.randint(0, 100) for _ in range (50)] 
    arr.sort()

    target = random.randint(0, 100)

    print(arr)
    print(target)

    result = binary_search(arr, target, 0, len(arr) - 1)

    if not  result:
        print("존재하지 않습니다.")
    else :
        print(result)