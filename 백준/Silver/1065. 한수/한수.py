A = int(input())
B = 0

if A <= 99:
    B += A
    print(B)

elif A >= 0:
    for i in range(100,A+1):
        C = list(str(i))
        D = list(map(int,C))

        if D[1] - D[0] == D[2] - D[1]:
            B += 1
    B += 99
    print(B)