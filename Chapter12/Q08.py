N = input()

charlist = []
numlist = []

for i in N :
    if i in '1234567890' :
        numlist.append(int(i))
    else :
        charlist.append(i)
if numlist :
    print("".join(sorted(charlist)) + str(sum(numlist)))
else :
    print("".join(sorted(charlist)))