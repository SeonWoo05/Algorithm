A = []

for i in range(9):
    X = int(input())
    A.append(X)

total = 100
B = []

for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i] + A[j] + total == sum(A):
            B.append(A[i])
            B.append(A[j])


for i in A:
    if i not in B:
        print(i)