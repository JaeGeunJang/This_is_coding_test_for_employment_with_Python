def quickSort(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    sort_list = array[1:]

    left_side = [x for x in sort_list if x < pivot]
    right_side = [x for x in sort_list if x >= pivot]

    return quickSort(left_side) + [pivot] + quickSort(right_side)

if __name__ == "__main__" :
    import random
    array = [random.randint(0, 100) for _ in range(50)]
    print(array)
    print(quickSort(array))