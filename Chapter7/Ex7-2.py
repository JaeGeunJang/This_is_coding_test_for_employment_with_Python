import time, random
from Binary_Search_recur import binary_search

target = 50000
N = [random.randint(0, target) for _ in range (target//2)]
M = [random.randint(0, target) for _ in range (target//5)]

result = {'Counting' : [], "Binary" : [], "In" : []}
times = {'Counting' : 0, "Binary" : 0, "In" : 0}
search_list = ["Counting", "Binary", "In"]

start = time.time()
for m in M :
    if m in N :
        result["In"].append(True)
    else :
        result["In"].append(False)
end = time.time()
times["In"] = end - start

start = time.time()
N_counting = [0] * (target + 1)
for n in N :
    N_counting[n] += 1
for m in M :
    if N_counting[m] != 0 :
        result["Counting"].append(True)
    else :
        result["Counting"].append(False)
end = time.time()
times["Counting"] = end - start

start = time.time()
N.sort()
for m in M :
    if binary_search(N, m, 0, target-1) == False :
        result["Binary"].append(False)
    else :
        result["Binary"].append(True)
end = time.time()
times["Binary"] = end - start

if result["Binary"] == result['Counting'] == result["In"] :
    print("YES")
    print(times)
else :
    print(result["Binary"])
    print(result["Counting"])
    print(result["In"])
# result : {'Counting': 0.018927812576293945, 'Binary': 0.3563499450683594, 'In': 3.4288456439971924}
# Counting = O(n), Binary = O(n lg n), In = O(n^2)