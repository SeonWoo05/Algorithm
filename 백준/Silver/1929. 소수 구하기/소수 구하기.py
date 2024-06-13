def find_sosu(a,b):
    C = []
    for i in range(a,b+1):
        if i == 1:
            continue
        else:
            C.append(i)
    B = []

    for i in C:
        for j in range(2,int(i**(1/2))+1):
            if i % j == 0:
                break
        else:
            B.append(i)
    return B
                

a,b = map(int, input().split())
for i in find_sosu(a,b):
    print(i) 