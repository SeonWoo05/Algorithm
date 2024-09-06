A = []

for _ in range(9):
    B = list(map(int, input().split()))
    A.append(B)

maxint = 0
for i in range(9):
    for j in range(9):
        if maxint < A[i][j]:
            maxint = A[i][j]

print(maxint)

for i, row in enumerate(A):  # i는 행의 인덱스, row는 각 행(리스트)
        if maxint in row:
            print(i+1, row.index(maxint)+1)
            break