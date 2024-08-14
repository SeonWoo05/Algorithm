N = int(input())

A = []
for i in range(2,N+1):
    A.append(i)

B = []
for i in A:
    if N % i == 0:
        while N % i == 0:
            N = N / i
            B.append(i)

for i in B:
    print(i)