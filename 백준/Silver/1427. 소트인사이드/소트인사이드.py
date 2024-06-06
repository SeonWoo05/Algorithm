A = input()
A = list(map(int,A))
A.sort(reverse=True)
B = []

for i in A:
    B.append(str(i))
C = ''.join(B)
print(C)