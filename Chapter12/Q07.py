N = list(map(int, input()))
if sum(N[:len(N)//2]) == sum(N[len(N)//2:]) :
    print('LUCKY')
else :
    print("READY")