def selection_sort(array) :
    for i in range(len(array)-1) :
        min_index = i
        for j in range (i+1, len(array)) :
            if array[min_index] > array[j] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

if __name__ == "__main__" :
    import random
    array = [random.randint(0, 100) for _ in range(50)]
    print(array)
    print(selection_sort(array))