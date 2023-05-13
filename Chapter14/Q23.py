N = N = int(input())
n_list = []
for _ in range (N) :
    ns = input().split()
    ns = [ns[0]] + list(map(int, ns[1:]))
    n_list.append(ns)
n_list = sorted(n_list, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for n in n_list :
    print(n[0])