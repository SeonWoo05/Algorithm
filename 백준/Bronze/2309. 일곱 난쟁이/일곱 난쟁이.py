A = []
for i in range(9):
    x = int(input())
    A.append(x)

B = []
for i in range(8):
    for j in range(i+1,9):
        if A[i] + A[j] == sum(A) - 100:
            B.append(A[i])
            B.append(A[j])
            break

A.remove(B[0])
A.remove(B[1])
A.sort()

for i in A:
    print(i)
