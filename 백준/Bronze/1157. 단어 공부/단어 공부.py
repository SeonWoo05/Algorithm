A = input()
A = A.upper()
B = {}

for i in A:
    if i in B:
        B[i] += 1
    else:
        B[i] = 1

max_count = max(B.values())
max_char = [char for char, count in B.items() if count == max_count]

if len(max_char) != 1:
    print('?')

else:
    print(max_char[0])