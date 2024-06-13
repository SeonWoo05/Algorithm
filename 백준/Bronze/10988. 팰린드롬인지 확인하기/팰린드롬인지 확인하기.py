A = input()
B = []
for i in A:
    B.append(i)
if B == list(reversed(B)):
    print(1)

else:
    print(0)