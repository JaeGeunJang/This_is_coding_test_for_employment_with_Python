def counting_sort(array) :
    max_value = max(array)+1
    
    sorted_result = [0] * max_value 
    for i in range(len(array)) :
        sorted_result[array[i]] += 1

    result = []
    for i in range(max_value) :
        for _ in range (sorted_result[i]) :
            result.append(i)

    return result

if __name__ == "__main__" :
    import random
    array = [random.randint(0, 100) for _ in range(50)]
    print(array)
    print(counting_sort(array))