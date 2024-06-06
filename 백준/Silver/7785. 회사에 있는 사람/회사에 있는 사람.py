N = int(input())
A = {}

for i in range(N):
    x,y = input().split()
    if y == 'enter':
        A[x] = y
    elif y == 'leave':
        A.pop(x)

for i in sorted(A,reverse=True):
    print(i)