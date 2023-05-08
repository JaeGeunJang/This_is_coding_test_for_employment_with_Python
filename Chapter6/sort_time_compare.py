import random, time
from copy import deepcopy
from InsertSort import InsertSort
from QuickSort import quickSort
from SelectionSort import selection_sort
from CountingSort import counting_sort
array_num = 5000

array = [random.randint(0, array_num * 2) for _ in range(array_num)]
timedic = {}

array1 = deepcopy(array)
array2 = deepcopy(array)
array3 = deepcopy(array)
array4 = deepcopy(array)

start_time = time.time()
array1 = InsertSort(array1)
end_time = time.time()
timedic['Insert'] = end_time - start_time

start_time = time.time()
array2 = selection_sort(array2)
end_time = time.time()
timedic['Selection'] = end_time - start_time

start_time = time.time()
array3 = quickSort(array3)
end_time = time.time()
timedic['Quick'] = end_time - start_time

start_time = time.time()
array4 = counting_sort(array4)
end_time = time.time()
timedic['Counting'] = end_time - start_time

def check_sort(array1, array2, array3) :
    if not(len(array1) == len(array2) and len(array2) == len(array3) and len(array3) == len(array4)) :
        print("갯수가 맞지 않습니다.")
        return False
    
    for i in range (len(array1)) :
        if not (array1[i] == array2[i] and array2[i] == array3[i] and array3[i] == array4[i]) :
            print("정렬 순서가 같지 않습니다.")
            return False
        
    return True

if check_sort(array1, array2, array3) :
    for i in timedic.keys() :
        print("{} : {} sec".format(i, timedic[i]))
else :
    print("정렬이 잘 못 되었습니다.")